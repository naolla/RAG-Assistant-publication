from typing import List


def test_load_documents_smoke(monkeypatch) -> None:
    """Ensure the document loader returns a list without raising errors.

    This is a smoke test that calls the public loader and verifies the
    return type to catch obvious regressions in IO and parsing.
    """
    from src import app as app_module

    docs: List[dict] = app_module.load_documents()
    assert isinstance(docs, list)


def test_vectordb_chunking_and_add(monkeypatch) -> None:
    """Verify VectorDB adds chunked documents and invokes collection.add.

    Heavy dependencies are monkeypatched to keep the test fast and hermetic.
    """
    from src import vectordb as vdb_module

    class DummyEmbedder:
        def __init__(self, *args, **kwargs) -> None:
            pass

        def encode(self, texts, convert_to_numpy: bool = False):
            # Return deterministic fixed-size vectors
            import numpy as np

            if isinstance(texts, str):
                texts = [texts]
            arr = np.zeros((len(texts), 5), dtype=float)
            for i, t in enumerate(texts):
                arr[i, :] = len(t) % 7
            return arr if convert_to_numpy else arr.tolist()

    monkeypatch.setattr(vdb_module, "SentenceTransformer", DummyEmbedder)

    class DummyCollection:
        def __init__(self) -> None:
            self.add_calls: List[dict] = []

        def add(self, ids, documents, metadatas, embeddings) -> None:
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
        def __init__(self, *args, **kwargs) -> None:
            self.collection = DummyCollection()

        def get_or_create_collection(self, name, metadata):
            return self.collection

    monkeypatch.setattr(vdb_module.chromadb, "PersistentClient", DummyClient)

    db = vdb_module.VectorDB()
    docs = [{"content": "Hello world. This is a test document.", "metadata": {"source": "x.txt"}}]
    db.add_documents(docs)
    assert db.collection.add_calls, "Expected add() to be called with chunk data"


