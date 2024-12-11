import torch
from torch.profiler import profile, ProfilerActivity
from transformers import AutoTokenizer

from torch2onnx import TransformerModel

def calculate_flops():
    model = TransformerModel()
    model.eval()

    tokenizer = AutoTokenizer.from_pretrained("distilbert-base-cased")
    sample_text = "This is a test sentence."
    inputs = tokenizer(sample_text, return_tensors="pt", truncation=True, padding=True)

    input_ids, attention_mask = inputs["input_ids"], inputs["attention_mask"]

    with profile(activities=[ProfilerActivity.CPU], record_shapes=True) as prof:
        with torch.no_grad():
            model(input_ids, attention_mask)

    print(prof.key_averages().table(sort_by="cpu_time_total", row_limit=10))
    return prof.key_averages()

if __name__ == "__main__":
    calculate_flops()

