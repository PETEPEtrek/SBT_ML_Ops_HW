#!/bin/bash


onnx_model="models/distilbert_base_cased.onnx"

declare -a precisions=("FP32" "--fp16" "--int8" "--best")

for precision in "${precisions[@]}"; do
    trtexec \
    --onnx=$onnx_model \
    --saveEngine="models/model_${precision}.plan" \
    --minShapes=INPUT_IDS:1x16,ATTENTION_MASK:1x16 \
    --optShapes=INPUT_IDS:4x16,ATTENTION_MASK:4x16 \
    --maxShapes=INPUT_IDS:8x16,ATTENTION_MASK:8x16 \
    $precision
done

