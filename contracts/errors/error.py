from pydantic import BaseModel, Field
from typing import Optional, Literal, Dict, Any


class ErrorDetail(BaseModel):
    """
    Optional structured metadata about an error.\n
    Used for debugging or client-side handling.
    """
    field: Optional[str] = None
    info: Optional[Dict[str, Any]] = None


class ErrorContract(BaseModel):
    """
    Canonical error contract for the entire system.\n
    Used by REST APIs and SSE streams.
    """

    code: Literal[
        "VALIDATION_ERROR",
        "PARSING_ERROR",
        "LLM_ERROR",
        "STREAM_ERROR",
        "RATE_LIMIT_ERROR",
        "INTERNAL_ERROR"
    ] = Field(
        ...,
        description="Stable machine-readable error code"
    )

    message: str = Field(
        ...,
        description="Human-readable error message"
    )

    recoverable: bool = Field(
        ...,
        description="Whether the client can safely retry or recover"
    )

    details: Optional[ErrorDetail] = Field(
        default=None,
        description="Optional structured metadata about the error"
    )