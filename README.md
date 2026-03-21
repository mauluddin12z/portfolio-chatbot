# 🤖 AI Portfolio Chatbot (FAQ + RAG + Caching)

An intelligent chatbot built as a **portfolio assistant** for *Muhammad Hidayat Mauluddin*.
This project demonstrates a **production-ready AI system** using a hybrid approach: **FAQ → Cache → RAG → LLM**, optimized for performance and cost efficiency.

---

## 🚀 Key Features

* ⚡ **FAQ System** — instant responses without LLM usage
* 🧠 **RAG (Retrieval-Augmented Generation)** with FAISS
* 🔎 **Semantic Search** using Sentence Transformers (MiniLM)
* 🤖 **Gemini AI Integration** for contextual answers
* 💾 **Response Caching** (reduces token usage significantly)
* ⛔ **Rate Limiting** (10 requests/day per user)
* 🛡️ **Input Validation** (anti-spam & prompt injection protection)

---

## 🧠 System Architecture

```
User Request
     ↓
Validation
     ↓
Rate Limiting
     ↓
FAQ (instant, no cost)
     ↓
Cache (instant, no cost)
     ↓
RAG (FAISS retrieval)
     ↓
LLM (Gemini)
     ↓
Response
```

---

## 📁 Project Structure

```
app/
├── api/routes/chat.py        # API endpoint
├── services/
│   ├── ai_service.py         # Gemini integration
│   ├── rag_service.py        # FAISS + embeddings
│   ├── faq_service.py        # FAQ lookup
│   └── cache_service.py      # in-memory cache
├── utils/
│   ├── rate_limiter.py       # daily limit
│   └── validator.py          # input validation
├── schemas/
│   └── chat_schema.py        # request schema
├── data/
│   ├── knowledge.json        # RAG knowledge base
│   └── faq.json              # FAQ data
└── main.py
```

---

## ⚙️ Installation

```bash
git clone https://github.com/mauluddin12z/portfolio-chatbot
cd portfolio-chatbot

python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate  # Mac/Linux

pip install -r requirements.txt
```

---

## 🔑 Environment Setup

Create a `.env` file:

```
GEMINI_API_KEY=your_api_key_here
```

---

## ▶️ Run the Application

```bash
uvicorn app.main:app --reload
```

API will be available at:

```
http://127.0.0.1:8000
```

---

## 📡 API Usage

### POST `/chat`

#### Request

```json
{
  "question": "What is your experience in machine learning?"
}
```

#### Response

```json
{
  "source": "rag",
  "context": [...],
  "answer": "..."
}
```

---

## 🧪 Response Sources

| Source  | Description                             |
| ------- | --------------------------------------- |
| `faq`   | Answer from predefined FAQ (no AI cost) |
| `cache` | Cached response                         |
| `rag`   | Generated using RAG + Gemini            |

---

## 🛡️ Optimization & Safety

* Daily request limit per user (IP-based)
* Input length & content validation
* Prompt injection prevention
* LLM token usage control
* Response caching with TTL

---

## 🧰 Tech Stack

* **Backend:** FastAPI
* **Vector Store:** FAISS
* **Embeddings:** Sentence Transformers (MiniLM)
* **LLM:** Gemini API
* **Language:** Python

---

## 🎯 Why This Project Matters

This project showcases:

* Real-world **RAG implementation**
* **Cost optimization strategies** for LLM systems
* Clean and modular backend architecture
* Practical AI system design (not just model usage)

---

## 🚧 Future Improvements

* Redis-based distributed caching
* Semantic FAQ matching (embedding-based)
* User authentication system
* Analytics dashboard (question tracking)

---

## 👨‍💻 Author

**Muhammad Hidayat Mauluddin**
Full-Stack Web Developer | Machine Learning Enthusiast

---

## ⭐ Notes

This project is built as part of a **portfolio to demonstrate practical AI engineering skills**, focusing on scalability, efficiency, and clean architecture.
