from pydantic import BaseModel, Field
from typing import List, Optional


# COMMON SUB-STRUCTURES

class ResumeBullet(BaseModel):
    text: str


class ResumeEntry(BaseModel):
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


# ROOT PARSED RESUME SCHEMA
class ParsedResume(BaseModel):
    """
    Canonical parsed resume schema.\n
    Output of resume parsing + normalization.
    """

    summary: Optional[ResumeSummary] = None
    experience: Optional[ResumeExperience] = None
    education: Optional[ResumeEducation] = None
    projects: Optional[ResumeProjects] = None
    skills: Optional[ResumeSkills] = None