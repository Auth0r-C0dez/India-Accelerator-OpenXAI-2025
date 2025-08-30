from transformers import AutoTokenizer

MODEL_PATH = r"E:\Intrnships\blockSeBlock\Task2\Backend\model\summarizer"
tokenizer = AutoTokenizer.from_pretrained("EleutherAI/gpt-neo-1.3B")
tokenizer.save_pretrained(MODEL_PATH)
