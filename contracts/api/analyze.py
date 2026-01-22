from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class AnalyzeRequest(BaseModel):
    """
    Contract for initiating a resume analysis request.
    """

    email: EmailStr = Field(
        ...,
        description="User's email address"
    )

    generate_modified_resume: bool = Field(
        default=False,
        description="Whether the system should generate a rewritten resume"
    )

    focus: Optional[str] = Field(
        default=None,
        description=(
            "Optional user-provided focus or instruction, "
            "e.g. 'backend roles', 'ML engineer', 'concise resume'"
        )
    )