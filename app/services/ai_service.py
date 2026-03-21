from google import genai
from app.core.config import GEMINI_API_KEY


class AIService:
    def __init__(self):
        self.client = genai.Client(api_key=GEMINI_API_KEY)

    def _build_prompt(self, question: str, context_chunks: list):
        context = "\n\n".join(
            [f"- {chunk}" for chunk in context_chunks]
        )

        return f"""
You are a professional portfolio assistant for Muhammad Hidayat Mauluddin.

Your task is to answer recruiter questions based ONLY on the provided context.

=====================
CONTEXT:
{context}
=====================

RULES:
- Only use information from CONTEXT
- Do NOT add assumptions or external knowledge
- Keep the answer concise (max 3 sentences)
- Use a professional and confident tone

QUESTION:
{question}

ANSWER:
"""

    def generate_response(self, question: str, context_chunks: list):
        # Safety: if there is no context
        if not context_chunks:
            return "Please contact me directly for more information."

        prompt = self._build_prompt(question, context_chunks)

        try:
            response = self.client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt,
                config={
                    "temperature": 0.3,
                    "top_p": 0.9,
                    "max_output_tokens": 200
                }
            )

            # handle response
            if not response or not response.text:
                return "Please contact me directly for more information."

            return response.text.strip()

        except Exception as e:
            print("Gemini Error:", e)
            return "Error generating response."


ai_service = AIService()