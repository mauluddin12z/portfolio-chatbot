from fastapi import APIRouter, Request, HTTPException
from app.services.faq_service import faq_service
from app.services.rag_service import rag_service
from app.services.ai_service import ai_service
from app.utils.rate_limiter import is_allowed
from app.utils.validator import validate_question
from app.services.cache_service import cache_service
from app.schemas.chat_schema import ChatRequest

router = APIRouter()


@router.post("/chat")
async def chat(request: Request, body: ChatRequest):
    question = body.question

    # 1. VALIDATION
    valid, error = validate_question(question)
    if not valid:
        raise HTTPException(status_code=400, detail=error)

    # 2. RATE LIMIT
    user_id = request.client.host
    if not is_allowed(user_id):
        raise HTTPException(status_code=429, detail="Limit reached")

        # FAQ FIRST (IMPORTANT)
    faq_answer = faq_service.find_answer(question)
    if faq_answer:
        return {"source": "faq", "answer": faq_answer}

    # 3. CACHE CHECK
    cached = cache_service.get(question)
    if cached:
        return {
            "source": "cache",
            "context": cached["context"],
            "answer": cached["answer"],
        }

    # 3. RAG
    context = rag_service.search(question)

    # 4. AI
    answer = ai_service.generate_response(question, context)

    return {"source": "rag", "context": context, "answer": answer}
