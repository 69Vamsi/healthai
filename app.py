from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import requests

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
import os
HF_API_KEY = os.getenv("HF_API_KEY")
MODEL_URL = os.getenv("MODEL_URL")
MODEL_URL = "https://api-inference.huggingface.co/models/distilbert-base-uncased-finetuned-sst-2-english"
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

# Load FLAN-T5 model and tokenizer once during startup
MODEL_NAME = "google/flan-t5-small"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)

def query_hf(prompt: str) -> str:
    try:
        # Tokenize the input prompt
        inputs = tokenizer(prompt, return_tensors="pt", truncation=True)
        # Generate output
        outputs = model.generate(**inputs, max_new_tokens=150)
        # Decode the generated response
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        return response
    except Exception as e:
        print("❌ Local Inference Error:", e)
        return "Sorry, I couldn't process your request locally."


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "result": None})

@app.post("/symptom", response_class=HTMLResponse)
async def symptom_identifier(request: Request, symptoms: str = Form(...)):
    try:
        prompt = f"<think>User reports these symptoms: {symptoms}. What is the most likely disease or condition?</think><response>"
        result = query_hf(prompt)
        return templates.TemplateResponse("index.html", {"request": request, "result": result})
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")

@app.post("/remedy", response_class=HTMLResponse)
async def home_remedy(request: Request, disease: str = Form(...)):
    prompt = f"<think>Suggest a safe, natural home remedy for {disease}. Only provide remedies suitable for general use and mention when to see a doctor.</think><response>"
    result = query_hf(prompt)
    return templates.TemplateResponse("index.html", {"request": request, "result": result})

@app.post("/chat", response_class=HTMLResponse)
async def patient_chat(request: Request, question: str = Form(...)):
    prompt = f"<think>User asks: {question}. Provide a clear, empathetic, and evidence-based answer. Acknowledge limitations and suggest when to seek professional medical advice.</think><response>"
    result = query_hf(prompt)
    return templates.TemplateResponse("index.html", {"request": request, "result": result})

@app.post("/analytics", response_class=HTMLResponse)
async def health_analytics(request: Request, metrics: str = Form(...)):
    prompt = f"<think>User provides health metrics: {metrics}. Analyze the data, visualize trends if possible, and provide recommendations or insights about potential health concerns.</think><response>"
    result = query_hf(prompt)
    return templates.TemplateResponse("index.html", {"request": request, "result": result})
