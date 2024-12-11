from typing import Any

import torch
import numpy as np
import onnxruntime as ort
from transformers import AutoModel, AutoTokenizer
from ptflops import get_model_complexity_info
from thop import profile

class TextHeadWithProj(torch.nn.Module):
    def __init__(self, text_model_name: str, output_dim: int):
        super().__init__()
        self.backbone = AutoModel.from_pretrained(
            text_model_name,
            return_dict=True,
            output_hidden_states=True,
        )
        self.fc = torch.nn.Linear(self.backbone.config.hidden_size, output_dim)

    def forward(self, input_ids, attention_mask):
        outputs = self.backbone(input_ids, attention_mask=attention_mask)
        last_hidden_state = outputs.last_hidden_state
        
        embedding = last_hidden_state[:, 0, :]
        
        proj = self.fc(embedding)
        return proj


def encode(tokenizer: Any, text: str, max_len: int):
    encoded = tokenizer.encode_plus(
        text, padding="max_length", max_length=max_len, truncation=True
    )
    input_ids = torch.tensor(encoded["input_ids"], dtype=torch.int32, device="cpu")
    attention_mask = torch.tensor(
        encoded["attention_mask"], dtype=torch.int32, device="cpu"
    )
    return input_ids, attention_mask

def main():
    model_name = "distilbert-base-cased"
    output_proj_dim = 96

    model = TextHeadWithProj(model_name, output_proj_dim)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model.eval()

    texts = ["One two three", "Four six seven"]
    tokens_tensor, att_mask_tensor = [], []
    for text in texts:
        _tokens, _mask = encode(tokenizer, text, 16)
        tokens_tensor.append(_tokens)
        att_mask_tensor.append(_mask)

    tokens_tensor = torch.stack(tokens_tensor)
    att_mask_tensor = torch.stack(att_mask_tensor)

    torch.onnx.export(
        model,
        (tokens_tensor, att_mask_tensor),
        "models/distilbert_base_cased_embedder.onnx",
        export_params=True,
        opset_version=19,
        input_names=["INPUT_IDS", "ATTENTION_MASK"],
        output_names=["EMBEDDINGS"],
        dynamic_axes={
            "INPUT_IDS": {0: "BATCH_SIZE"},
            "ATTENTION_MASK": {0: "BATCH_SIZE"},
            "EMBEDDINGS": {0: "BATCH_SIZE"},
        },
    )

    original_embeddings = model(tokens_tensor, att_mask_tensor).detach().numpy()
    ort_inputs = {
        "INPUT_IDS": tokens_tensor.numpy(),
        "ATTENTION_MASK": att_mask_tensor.numpy(),
    }
    ort_session = ort.InferenceSession("models/distilbert_base_cased_embedder.onnx")
    onnx_embeddings = ort_session.run(None, ort_inputs)[0]

    assert np.allclose(original_embeddings, onnx_embeddings, atol=1e-5)

if __name__ == "__main__":
    main()
