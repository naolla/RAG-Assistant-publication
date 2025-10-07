# RAG Based Publication Assistant

## 🤖 What is this?

RAG Based Publication Assistant is a Retrieval-Augmented Generation (RAG) application that ingests publication files (research articles, notes, and text documents), indexes them in a vector database, and answers questions using relevant excerpts from those publications.

**Think of it as:** a focused assistant that answers questions grounded in your publication library.

## 🎯 What it does

This assistant can:

- 📄 **Load your documents** (PDFs, text files, etc.)
- 🔍 **Search through them** to find relevant information
- 💬 **Answer questions** using the information it found
- 🧠 **Combine multiple sources** to give comprehensive answers

 
---

## 🚀 Quick Start

1) Install (prefer the lockfile for reproducibility)
```bash
pip install -r requirements.lock
```

2) Configure one provider API key in a `.env` file
```
OPENAI_API_KEY=...
# or GROQ_API_KEY=...
# or GOOGLE_API_KEY=...
```

3) Run
```bash
python -m src.app
```

Docker (optional)
```bash
docker build -f ops/docker/Dockerfile -t rag-assistant .
docker run --rm -it --env-file .env rag-assistant
```

## ⚙️ Configuration

- Place text files in `data/` (default loader reads `*.txt`).
- Environment variables:
  - `CHROMA_COLLECTION_NAME` (default: `rag_documents`)
  - `EMBEDDING_MODEL` (default: `sentence-transformers/all-MiniLM-L6-v2`)
  - `LOG_LEVEL` (default: `INFO`)

See `src/config.py` for centralized settings.

## 🧠 Architecture

- `src/app.py`: RAG assistant, prompt, and query pipeline
- `src/vectordb.py`: Chunking, embeddings, ChromaDB storage and search
- `data/`: Your publication files (txt by default)
- `tests/`: Basic tests with dependency monkeypatching

## 📚 Documentation

- API: `docs/API.md`
- GPU: `docs/GPU.md`
- Contributing: `CONTRIBUTING.md`
- Changelog: `CHANGELOG.md`
- Code of Conduct: `CODE_OF_CONDUCT.md`
- License: `LICENSE`
- Copyright: `COPYRIGHT`
