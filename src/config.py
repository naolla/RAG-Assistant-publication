import os
from dataclasses import dataclass
from pathlib import Path
import yaml


@dataclass(frozen=True)
class Settings:
    chroma_collection_name: str
    embedding_model: str
    log_level: str


def get_settings() -> Settings:
    # Load from YAML if present
    yaml_path = Path(__file__).resolve().parent.parent / "config" / "settings.yaml"
    yaml_example = Path(__file__).resolve().parent.parent / "config" / "settings.example.yaml"

    data = {}
    path_to_use = None
    for candidate in (yaml_path, yaml_example):
        if candidate.exists():
            path_to_use = candidate
            try:
                with open(candidate, "r", encoding="utf-8") as f:
                    data = yaml.safe_load(f) or {}
            except Exception:
                data = {}
            break

    chroma_collection_name = os.getenv(
        "CHROMA_COLLECTION_NAME", data.get("chroma_collection_name", "rag_documents")
    )
    embedding_model = os.getenv(
        "EMBEDDING_MODEL",
        data.get("embedding_model", "sentence-transformers/all-MiniLM-L6-v2"),
    )
    log_level = os.getenv("LOG_LEVEL", data.get("log_level", "INFO"))

    return Settings(
        chroma_collection_name=chroma_collection_name,
        embedding_model=embedding_model,
        log_level=log_level,
    )


