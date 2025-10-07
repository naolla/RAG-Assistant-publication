import types


def test_load_documents_smoke(monkeypatch):
    from src import app as app_module

    # Point data loader to a temporary file set by monkeypatching glob
    docs = app_module.load_documents()
    assert isinstance(docs, list)


def test_vectordb_chunking_and_add(monkeypatch):
    # Monkeypatch SentenceTransformer to avoid heavy model load
    from src import vectordb as vdb_module

    class DummyEmbedder:
        def __init__(self, *args, **kwargs):
            pass

        def encode(self, texts, convert_to_numpy=False):
            # Return deterministic fixed-size vectors
            import numpy as np

            if isinstance(texts, str):
                texts = [texts]
            arr = np.zeros((len(texts), 5), dtype=float)
            for i, t in enumerate(texts):
                arr[i, :] = len(t) % 7
            return arr if convert_to_numpy else arr.tolist()

    monkeypatch.setattr(vdb_module, "SentenceTransformer", DummyEmbedder)

    # Monkeypatch chromadb client and collection
    class DummyCollection:
        def __init__(self):
            self.add_calls = []

        def add(self, ids, documents, metadatas, embeddings):
            self.add_calls.append(
                {
                    "ids": ids,
                    "documents": documents,
                    "metadatas": metadatas,
                    "embeddings": embeddings,
                }
            )

        def query(self, query_embeddings, n_results, include):
            return {"documents": [["dummy"]], "metadatas": [[{}]], "distances": [[0.0]], "ids": [["x"]]}

    class DummyClient:
        def __init__(self, *args, **kwargs):
            self.collection = DummyCollection()

        def get_or_create_collection(self, name, metadata):
            return self.collection

    monkeypatch.setattr(vdb_module.chromadb, "PersistentClient", DummyClient)

    db = vdb_module.VectorDB()
    docs = [{"content": "Hello world. This is a test document.", "metadata": {"source": "x.txt"}}]
    db.add_documents(docs)
    # Ensure something was added
    assert db.collection.add_calls, "Expected add() to be called with chunk data"


