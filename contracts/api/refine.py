from pydantic import BaseModel, EmailStr, Field
from typing import Literal, Optional


class RefineRequest(BaseModel):
    """
    Contract for refining or regenerating parts of a previous analysis.\n
    Starts a new SSE stream.
    """

    email: EmailStr = Field(
        ...,
        description="User's email address"
    )

    parent_request_id: str = Field(
        ...,
        description="Request ID of the original analysis being refined"
    )

    refine_type: Literal[
        "full_regeneration",
        "section_regeneration",
        "analysis_refocus"
    ] = Field(
        ...,
        description="Type of refinement requested"
    )

    target_section: Optional[Literal[
        "summary",
        "experience",
        "skills",
        "education",
        "projects"
    ]] = Field(
        default=None,
        description=(
            "Required if refine_type is 'section_regeneration'. Ignored otherwise."
        )
    )

    user_feedback: str = Field(
        ...,
        min_length=5,
        description=(
            "User-provided feedback or instruction explaining what should be improved or changed"
        )
    )