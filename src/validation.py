from typing import Any, Dict
from pydantic import BaseModel, Field, ValidationError


class Document(BaseModel):
    content: str = Field(min_length=1)
    metadata: Dict[str, Any] = Field(default_factory=dict)


def validate_document(doc: Any) -> Document:
    return Document.model_validate(doc)


