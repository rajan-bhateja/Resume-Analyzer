from typing import Literal, Optional, Union
from pydantic import BaseModel


# BASE CLASS EVENT
class SSEBaseEvent(BaseModel):
    event: str


# LIFECYCLE EVENTS

# REQUESTED ACCEPTED EVENT
class RequestAcceptedEvent(SSEBaseEvent):
    event: Literal["request_accepted"]
    request_id: str


# RESUME PARSED EVENT
class ResumeParsedEvent(SSEBaseEvent):
    event: Literal["resume_parsed"]


# ANALYSIS COMPLETED EVENT
class AnalysisStepCompletedEvent(SSEBaseEvent):
    event: Literal["analysis_step_completed"]
    step: Literal[
        "skills_extracted",
        "skills_evaluated",
        "resume_criticized",
        "roles_recommended"
    ]


# RESUME SECTION GENERATED EVENT
class ResumeSectionGeneratedEvent(SSEBaseEvent):
    event: Literal["resume_section_generated"]
    section: str
    content: dict


# ANALYSIS COMPLETED EVENT
class AnalysisCompleteEvent(SSEBaseEvent):
    event: Literal["analysis_complete"]
    analysis: dict
    rewritten_resume: Optional[dict] = None


# ERROR EVENT
class ErrorEvent(SSEBaseEvent):
    event: Literal["error"]
    code: str
    message: str
    recoverable: bool = False


# Union Type (IMPORTANT)
SSEEvent = Union[
    RequestAcceptedEvent,
    ResumeParsedEvent,
    AnalysisStepCompletedEvent,
    ResumeSectionGeneratedEvent,
    AnalysisCompleteEvent,
    ErrorEvent
]