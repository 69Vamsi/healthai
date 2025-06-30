# 🩺 HealthAI - Symptom Analyzer & Medical Assistant (FastAPI + FLAN-T5)

HealthAI is a lightweight web application that allows users to:
- Analyze symptoms to suggest possible diseases.
- Get home remedies for common ailments.
- Ask health-related questions.
- Analyze health metrics for basic insights.

Built using **FastAPI** and powered by **Google FLAN-T5** (via Hugging Face Transformers) for local inference.

---

## 🚀 Features

- 🔍 Symptom-based disease prediction
- 🌿 Home remedies suggestions
- 💬 AI-powered health chat
- 📊 Health metric analysis
- 🧠 Local inference with FLAN-T5 (no API calls needed!)

---

## 📁 Project Structure

healthai/
├── app.py                  # Main FastAPI application  
├── templates/  
│   └── index.html          # HTML template for frontend  
├── static/                 # (Optional) For CSS/JS/image assets  
├── .env                    # (Not committed) Contains API keys (optional)  
├── requirements.txt        # Python dependencies  
└── README.md               # This file

---

## ⚙️ Requirements

- Python 3.8+
- pip

---

## 📦 Setup Instructions

### 1. Clone the Repository

### 2. Create Virtual Environment (Optional but Recommended)
python -m venv venv
venv\Scripts\activate # For Windows

OR
source venv/bin/activate # For macOS/Linux

shell
Copy
Edit

### 3. Install Dependencies
pip install -r requirements.txt

yaml
Copy
Edit

---

## 🔐 Environment Variables (Optional)

If you're using Hugging Face API:

Create a `.env` file with this format:
HF_API_KEY=your_huggingface_api_key
MODEL_URL=https://api-inference.huggingface.co/models/distilbert-base-uncased-finetuned-sst-2-english

yaml
Copy
Edit

But by default, the app uses the **FLAN-T5** model locally.

---

## 🧠 Run the App

uvicorn app:app --reload

yaml
Copy
Edit

Visit: http://127.0.0.1:8000  
API Docs: http://127.0.0.1:8000/docs

---

## ✅ Demo Use

Try:

- **Symptoms**: "fever, cough, sore throat"
- **Home Remedy**: "common cold"
- **Chat**: "Is walking good for heart health?"
- **Analytics**: "BP 130/90, weight 78kg, sugar 180 mg/dL"

---

## 📜 License

MIT License

---

## 🙏 Credits

- FastAPI — https://fastapi.tiangolo.com/
- Transformers — https://huggingface.co/docs/transformers
- FLAN-T5 by Google — https://huggingface.co/google/flan-t5-small