from chromadb import PersistentClient

from .base import VectorStore


class Chroma(VectorStore):
    def __init__(self) -> None:
        super().__init__()
        self.client = PersistentClient(path="./data/chroma")
        self.collection = self.client.get_or_create_collection("giftia")
        self.embedding = None

    def search(self, query: str, n_result: int):
        vec = self.embedding(query)
        results = self.collection.query(query_embeddings=[vec], n_results=n_result)
        return results["documents"][0]
