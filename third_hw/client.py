import numpy as np
import tritonclient.http as httpclient
from typing import List



def call_triton(input_text: str) -> List[np.ndarray]:

    TRITON_SERVER_URL = "localhost:8000"
    MODEL_NAME = "ensemble"

    client = httpclient.InferenceServerClient(url=TRITON_SERVER_URL)

    inputs = [httpclient.InferInput("TEXT", [1], "BYTES")]

    inputs[0].set_data_from_numpy(np.array([input_text.encode('utf-8')], dtype="object"))

    outputs = [
        httpclient.InferRequestedOutput("EMBEDDINGS_ONNX"),
        httpclient.InferRequestedOutput("EMBEDDINGS_FP16"),
        httpclient.InferRequestedOutput("EMBEDDINGS_FP32"),
        httpclient.InferRequestedOutput("EMBEDDINGS_INT8"),
        httpclient.InferRequestedOutput("EMBEDDINGS_BEST"),
    ]

    response = client.infer(MODEL_NAME, inputs, outputs=outputs)

    embeddings = [
        response.as_numpy("EMBEDDINGS_ONNX"),
        response.as_numpy("EMBEDDINGS_FP16"),
        response.as_numpy("EMBEDDINGS_FP32"),
        response.as_numpy("EMBEDDINGS_INT8"),
        response.as_numpy("EMBEDDINGS_BEST"),
    ]

    return [embedding.squeeze() for embedding in embeddings]


def check_quality(input_text: str) -> List[float]:

    embeddings = call_triton(input_text)
    onnx_embedding = embeddings[0]
    fp32_embedding = embeddings[1]

    deviations = [
        np.sqrt(np.mean((embedding - onnx_embedding) ** 2))
        for embedding in embeddings[1:]
    ]

    return deviations


def main():
    texts = [
        "This is a test sentence.",
        "Another example of input text.",
        "Deep learning models are powerful tools.",
        "Triton makes deployment easier.",
        "Let's evaluate the embeddings!",
    ]

    total_deviations = np.zeros(4)

    for text in texts:
        deviations = check_quality(text)
        total_deviations += np.array(deviations)
        print(f"Text: {text}")
        print(f"Deviations: {deviations}")

    avg_deviations = total_deviations / len(texts)

    print("\nAverage deviations:")
    print(f"FP16: {avg_deviations[0]:.5f}")
    print(f"FP32: {avg_deviations[1]:.5f}")
    print(f"INT8: {avg_deviations[2]:.5f}")
    print(f"BEST: {avg_deviations[3]:.5f}")


if __name__ == "__main__":
    main()
