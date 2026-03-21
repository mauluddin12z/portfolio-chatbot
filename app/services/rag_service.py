import json
import faiss
import numpy as np
import os
from sentence_transformers import SentenceTransformer

DATA_PATH = os.path.join(os.path.dirname(__file__), "../data/knowledge.json")

class RAGService:
    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

        with open(DATA_PATH, "r") as f:
            self.knowledge = json.load(f)

        self.texts = [item["text"] for item in self.knowledge]
        self.keywords = [item.get("keywords", []) for item in self.knowledge]

        self._build_index()
        print("Total vectors in index:", self.index.ntotal)

    def _build_index(self):
        embeddings = self.model.encode(self.texts)
        self.embeddings = np.array(embeddings).astype("float32")

        dim = self.embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dim)
        self.index.add(self.embeddings)


    # 🔥 QUERY EXPANSION
    def expand_query(self, query: str) -> str:
        q = query.lower()

        if "machine learning" in q or "ml" in q:
            q += " cnn unet ann deep learning ai model"

        if "backend" in q:
            q += " nodejs express api database"

        if "frontend" in q:
            q += " nextjs react ui"

        return q

    # 🔥 HYBRID SEARCH
    def search(self, query: str, k: int = 3):
        expanded_query = self.expand_query(query)

        q_embedding = self.model.encode([expanded_query])
        q_embedding = np.array(q_embedding).astype("float32")

        D, I = self.index.search(q_embedding, k)

        results = []

        for idx in I[0]:
            text = self.texts[idx]
            keywords = self.keywords[idx]

            keyword_score = 0

            for kw in keywords:
                if kw in query.lower():
                    keyword_score += 1

            results.append({
                "text": text,
                "keyword_score": keyword_score
            })

        # 🔥 Re sorting (HYBRID)
        results = sorted(
            results,
            key=lambda x: x["keyword_score"],
            reverse=True
        )

        return [r["text"] for r in results]


rag_service = RAGService()