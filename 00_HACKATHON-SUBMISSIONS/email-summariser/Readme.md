## For getting started with the project please follow 
https://docs.google.com/document/d/1qGkDdIVUw5l1tVgLj9F800X-vFOQWfsGuKPYAV2-pgo/edit?usp=sharing

# 📰 AI E-mail Summarizer 

A FastAPI-based FUll-Stack service that provides AI-powered text summarization using a locally hosted GPT-Neo model.
This project demonstrates how to run state-of-the-art transformer models offline and expose them as a REST API that can integrate with any frontend.

## 🚀 Features

- Summarizes long articles, documents, or plain text
- Runs locally without external API calls (no OpenAI/paid API)
- Supports GPU acceleration (CUDA) if available
- Built with FastAPI for high performance and async support
- Includes CORS middleware for smooth frontend integration
- Extensible for other NLP tasks (e.g., Q&A, rewriting)

## 📂 Project Structure

blockSeBlock/
│
├── Task2/
│ ├── Backend/
│ │ ├── app.py # Main FastAPI application
│ │ ├── models/
│ │ │ └── summarizer/ # Local GPT-Neo model + tokenizer
│ │ ├── requirements.txt # Dependencies
│ │ └── README.md # Project documentation (this file)
│ └── Frontend/ # (Optional) Web UI consuming the API



## ⚙️ Tech Stack

- **Python 3.9+**
- **FastAPI** – REST API framework
- **Transformers (Hugging Face)** – Model & tokenizer handling
- **PyTorch** – Deep learning backend
- **Uvicorn** – ASGI server

## 🧠 Model Details

- **Base Model**: EleutherAI GPT-Neo-1.3B
- **Task**: Text summarization (prompt-based generation)
- **Tokenizer**: GPT-2 BPE tokenizer (with fallback if tokenizer.json is corrupted)
- **Device Support**:
  - Uses CUDA if available
  - Falls back to CPU otherwise

## 🔧 Installation & Setup

### 1️⃣ Clone the Repository

git clone https://github.com/your-username/blockSeBlock.git
cd blockSeBlock/Task2/Backend


### 2️⃣ Create Virtual Environment

python -m venv venv
source venv/bin/activate # On Mac/Linux
venv\Scripts\activate # On Windows


### 3️⃣ Install Dependencies

pip install -r requirements.txt



**requirements.txt** should contain:
fastapi
uvicorn
transformers
torch
pydantic



### 4️⃣ Download Model

Make sure the model files are inside:
Backend/models/summarizer/



If missing, download from Hugging Face:

from transformers import AutoTokenizer, AutoModelForCausalLM

MODEL_PATH = "./models/summarizer"
model = AutoModelForCausalLM.from_pretrained("EleutherAI/gpt-neo-1.3B")
tokenizer = AutoTokenizer.from_pretrained("EleutherAI/gpt-neo-1.3B")
model.save_pretrained(MODEL_PATH)
tokenizer.save_pretrained(MODEL_PATH)



## ▶️ Running the Server

Start the FastAPI app with Uvicorn:

uvicorn app:app --reload



Server will run at:
http://127.0.0.1:8000



## 🔌 API Endpoints

### POST /summarize

**Request**
{
"text": "Your long article or document text goes here..."
}


**Response**
{
"summary": "This is the AI-generated summary."
}



## 🖥️ Example Usage



### Python Client
import requests

url = "http://127.0.0.1:8000/summarize"
data = {"text": "FastAPI is a high-performance web framework..."}
res = requests.post(url, json=data)
print(res.json())



## 🌐 Frontend Integration

Since CORS is enabled, you can call this API directly from a frontend (React, Vue, Angular, plain JS). Example:

async function getSummary(articleText) {
const response = await fetch("http://127.0.0.1:8000/summarize", {
method: "POST",
headers: { "Content-Type": "application/json" },
body: JSON.stringify({ text: articleText })
});
const data = await response.json();
return data.summary;
}

text

## ⚠️ Troubleshooting

| Issue | Cause | Solution |
|-------|-------|----------|
| FileNotFoundError: tokenizer.json | Missing/corrupted tokenizer | Delete tokenizer.json, regenerate with AutoTokenizer.from_pretrained(...) |
| CUDA not detected | No GPU drivers / CUDA installed | Falls back to CPU automatically |
| Slow inference | Large model (1.3B params) | Use smaller model like gpt-neo-125M |
| HTTP 500 errors | Text too long | Increase max_length or chunk input |

## 📈 Performance Notes

- GPT-Neo-1.3B requires ~5GB VRAM for smooth GPU inference
- For CPU-only systems, inference will be slower (~10-20s per request)
- You can replace with a smaller model (gpt-neo-125M) if needed

## 🔮 Future Improvements

- Add asynchronous batch processing for multiple requests
- Expose a WebSocket endpoint for streaming summaries
- Fine-tune GPT-Neo specifically for summarization (improved quality)
- Add support for other tasks: paraphrasing, Q&A, document expansion

## 👨‍💻 Author

**Rana** – AI/ML enthusiast & developer.  
Part-time web developer, GenAI explorer, and aspiring freelancer.

**Made with hardwork by Rana**