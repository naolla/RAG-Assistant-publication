import logging
import os
from typing import Optional


def configure_logging(level: Optional[str] = None) -> None:
    """Configure root logging once with a sensible default format.

    Subsequent calls are no-ops if handlers already exist.
    """
    if logging.getLogger().handlers:
        return
    logging.basicConfig(
        level=(level or os.getenv("LOG_LEVEL", "INFO")),
        format="%(asctime)s %(levelname)s %(name)s - %(message)s",
    )


def get_logger(name: str) -> logging.Logger:
    """Return a module/class specific logger."""
    return logging.getLogger(name)


