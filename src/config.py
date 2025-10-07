import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    chroma_collection_name: str = os.getenv("CHROMA_COLLECTION_NAME", "rag_documents")
    embedding_model: str = os.getenv(
        "EMBEDDING_MODEL", "sentence-transformers/all-MiniLM-L6-v2"
    )
    log_level: str = os.getenv("LOG_LEVEL", "INFO")


def get_settings() -> Settings:
    return Settings()


