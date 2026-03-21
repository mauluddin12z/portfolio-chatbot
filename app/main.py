from fastapi import FastAPI
from app.api.chat import router as chat_router

app = FastAPI(title="Portfolio Chatbot API")

app.include_router(chat_router, prefix="/api")


@app.get("/")
def root():
    return {"message": "Portfolio Chatbot API is running"}
