import time

class CacheService:
    def __init__(self):
        self.cache = {}
        self.ttl = 60 * 60 * 24

    def _normalize(self, text: str) -> str:
        return text.lower().strip()

    def get(self, question: str):
        key = self._normalize(question)

        if key in self.cache:
            data = self.cache[key]

            # cek expired
            if time.time() - data["time"] < self.ttl:
                return data["value"]

            # hapus kalau expired
            del self.cache[key]

        return None

    def set(self, question: str, value):
        key = self._normalize(question)

        self.cache[key] = {
            "value": value,
            "time": time.time()
        }


cache_service = CacheService()