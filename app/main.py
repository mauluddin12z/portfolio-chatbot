import os
import json
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.chat import router as chat_router

app = FastAPI(title="Portfolio Chatbot API")

# CORS configuration
origins = [
    "http://localhost:3000",
    "http://192.168.0.105:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes
app.include_router(chat_router, prefix="/api")

knowledge_path = os.path.join(os.path.dirname(__file__), "./data/faq.json")


@app.get("/")
def root():
    return {"message": "Portfolio Chatbot API is running"}


@app.get("/api/faq")
def get_data():
    try:
        with open(knowledge_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"error": "JSON file not found"}
