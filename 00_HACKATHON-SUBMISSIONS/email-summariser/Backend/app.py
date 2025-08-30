from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Path to your saved model folder (update from "./model" → "./models/summarizer")
MODEL_PATH = "./model/summarizer"

# Check if CUDA is available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Load tokenizer and model once at startup
from transformers import AutoTokenizer, GPT2TokenizerFast

try:
    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH, local_files_only=True)
except Exception as e:
    print("⚠️ Failed to load fast tokenizer, falling back:", e)
    tokenizer = GPT2TokenizerFast.from_pretrained(MODEL_PATH, local_files_only=True)

model = AutoModelForCausalLM.from_pretrained(
    MODEL_PATH,
    torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
).to(device)

# Initialize FastAPI app
app = FastAPI()

# Enable CORS so frontend can access backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace "*" with frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define request schema
class ArticleRequest(BaseModel):
    text: str

@app.post("/summarize")
def summarize(request: ArticleRequest):
    prompt = f"Summarize the following article:\n{request.text}\nSummary:\n"

    # Tokenize input
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=512).to(device)

    # Generate summary
    output = model.generate(
        **inputs,
        max_length=300,
        num_beams=4,
        no_repeat_ngram_size=2,
        early_stopping=True
    )

    # Decode output
    summary = tokenizer.decode(output[0], skip_special_tokens=True)

    # Extract only the summary part if delimiter exists
    if "Summary:" in summary:
        summary = summary.split("Summary:")[-1].strip()

    return {"summary": summary}
