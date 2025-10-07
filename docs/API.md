# API and Parameters

## src.app.RAGAssistant

### __init__()
- Initializes LLM provider, vector DB, prompt template, and chain.

### add_documents(documents: list) -> None
- documents: List of dicts with keys:
  - content (str): required text
  - metadata (dict): optional metadata (e.g., source, path)

### invoke(input: str, n_results: int = 3) -> str
- input: User question.
- n_results: Top-k chunks to retrieve.
- Returns: Model answer as a string.

### query(question: str, n_results: int = 3) -> str
- Alias for `invoke`.

### load_documents() -> list[dict]
- Returns: List of `{ content: str, metadata: dict }` loaded from `data/*.txt`.

## src.vectordb.VectorDB

### __init__(collection_name: str | None = None, embedding_model: str | None = None)
- collection_name: Overrides `CHROMA_COLLECTION_NAME` (default `rag_documents`).
- embedding_model: Overrides `EMBEDDING_MODEL` (default HF MiniLM).

### chunk_text(text: str, chunk_size: int = 500) -> list[str]
- text: Input text to split.
- chunk_size: Approximate characters per chunk.
- Returns: List of chunks.

### add_documents(documents: list) -> None
- documents: List of dicts as above.
- Side effects: Embeds chunks and adds to Chroma collection.

### search(query: str, n_results: int = 5) -> dict
- query: Query string.
- n_results: Top-k.
- Returns: dict with `documents`, `metadatas`, `distances`, `ids` (lists).
