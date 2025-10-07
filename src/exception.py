from typing import Optional
from logger import get_logger


class AppError(Exception):
    """Base application error for consistent handling."""


def log_and_raise(message: str, *, cause: Optional[BaseException] = None) -> None:
    """Log an error and raise AppError, optionally chaining the original cause."""
    logger = get_logger(__name__)
    if cause is not None:
        logger.exception(message)
        raise AppError(message) from cause
    logger.error(message)
    raise AppError(message)


