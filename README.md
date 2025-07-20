# 🤖 Bhuvan's Chatbot

A lightweight local chatbot built using [TinyLlama-1.1B-Chat-v1.0](https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0), integrated with a Flask backend and HTML frontend. Includes instant replies for business-specific questions via a knowledge base.

---

## 📌 Features

- Locally runs TinyLlama using Hugging Face Transformers and PyTorch
- Flask API with `/ask` endpoint to generate chatbot responses
- HTML-based UI with loader animation and motivational quotes
- Fast response for known queries using an internal knowledge base

---

## 📁 Project Structure

.
├── app.py # Flask backend server
├── model.py # TinyLlama model logic + knowledge base
├── templates/
│ └── index.html # Frontend chatbot UI
├── requirements.txt
└── README.md

---

## 🚀 Getting Started

### Step 1: Clone the project
git clone https://github.com/your-username/tinyllama-chatbot.git
cd tinyllama-chatbot


Step 2: Create a virtual environment
python -m venv .venv
# Activate (Windows)
.venv\Scripts\activate
# Activate (macOS/Linux)
source .venv/bin/activate


Step 3: Install dependencies
pip install -r requirements.txt
🔌 Running the Project
▶️ Run the Flask API
python app.py
The server will start at:
http://localhost:5000



🌐 HTML Frontend
Open your browser and go to:
http://localhost:5000



UI Includes:
-Typing animation
-Loading spinner
-Rotating motivational quotes
-Final chatbot response



📬 API Usage (Manual Test)
POST http://localhost:5000/ask
Request Body:
{
  "question": "What is TorkeHub?"
}
Response:
{
  "answer": "TorkeHub is a white-label CRM used to automate business workflows..."
}



🧠 Knowledge Base (Fast Answers)
Some queries are instantly answered without using the LLM:
knowledge_base = {
  "what is torkehub": "...",
  "who built torkehub": "...",
  "what is tinyllama": "..."
}




✅ Requirements
flask
flask-cors
transformers
torch
Install them via:
pip install -r requirements.txt


📄 License
This project is intended for educational and internship task purposes only.


🙌 Credits
- TinyLlama – open-source LLM
- HuggingFace Transformers
- Flask for full-stack integration# ChatBot
