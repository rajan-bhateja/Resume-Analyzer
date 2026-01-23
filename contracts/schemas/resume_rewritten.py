from pydantic import BaseModel, Field
from typing import List, Optional, Literal


# COMMON SUB-STRUCTURES

class ResumeBullet(BaseModel):
    id: str = Field(
        ...,
        description="Stable identifier for bullet-level editing"
    )
    text: str


class ResumeEntry(BaseModel):
    id: str = Field(
        ...,
        description="Stable identifier for entry-level editing"
    )
    title: Optional[str] = None
    organization: Optional[str] = None
    location: Optional[str] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    bullets: List[ResumeBullet] = Field(default_factory=list)


# RESUME SECTIONS

class ResumeSummary(BaseModel):
    text: str


class ResumeExperience(BaseModel):
    entries: List[ResumeEntry]


class ResumeEducation(BaseModel):
    entries: List[ResumeEntry]


class ResumeProjects(BaseModel):
    entries: List[ResumeEntry]


class ResumeSkills(BaseModel):
    skills: List[str]


# SECTION WRAPPER

class ResumeSection(BaseModel):
    section: Literal[
        "summary",
        "experience",
        "education",
        "projects",
        "skills"
    ]
    content: object


# ROOT REWRITTEN RESUME SCHEMA

class RewrittenResume(BaseModel):
    """
    Canonical rewritten resume schema.\n
    Streamed section-by-section and edited client-side.
    """

    sections: List[ResumeSection]