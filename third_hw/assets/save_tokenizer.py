from transformers import AutoTokenizer


model_name = "distilbert-base-cased"


tokenizer = AutoTokenizer.from_pretrained(model_name)


output_dir = "."


tokenizer.save_pretrained(output_dir)



