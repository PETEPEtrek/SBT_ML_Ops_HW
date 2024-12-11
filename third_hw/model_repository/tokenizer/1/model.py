import os
import json
import torch
from transformers import AutoTokenizer
import triton_python_backend_utils as pb_utils
import numpy as np

class TritonPythonModel:
    def initialize(self, args):
        assets_path = "/assets/"
        self.tokenizer = AutoTokenizer.from_pretrained(assets_path)

    def execute(self, requests):
        responses = []
        for request in requests:
            text_input = request.inputs()[0].as_numpy()
            text_input = [text.decode("utf-8") for text in text_input]
            tokens = self.tokenizer(text_input, padding="max_length", truncation=True, max_length=16, return_tensors="pt")

            input_ids_output = pb_utils.Tensor("INPUT_IDS", tokens["input_ids"].numpy().astype(np.int32))
            attention_mask_output = pb_utils.Tensor("ATTENTION_MASK", tokens["attention_mask"].numpy().astype(np.int32))

            responses.append(pb_utils.InferenceResponse([input_ids_output, attention_mask_output]))
        return responses

