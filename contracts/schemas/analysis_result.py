from pydantic import BaseModel, Field
from typing import List, Optional, Literal


# SKILL EVALUATION

class SkillScore(BaseModel):
    name: str
    score: int = Field(
        ...,
        ge=0,
        le=100,
        description="Skill relevance or proficiency score (0–100)"
    )


class SkillEvaluation(BaseModel):
    skills: List[SkillScore]


# ROLE RECOMMENDATIONS

class RoleRecommendation(BaseModel):
    role: str
    confidence: int = Field(
        ...,
        ge=0,
        le=100,
        description="Confidence score for role suitability"
    )
    rationale: Optional[str] = Field(
        default=None,
        description="Short explanation for recommendation"
    )


class RoleRecommendations(BaseModel):
    roles: List[RoleRecommendation]


# RESUME ISSUES / GAPS

class ResumeIssue(BaseModel):
    category: Literal[
        "clarity",
        "impact",
        "skills",
        "structure",
        "experience",
        "formatting"
    ]
    message: str
    severity: Literal["low", "medium", "high"]


class ResumeCritique(BaseModel):
    issues: List[ResumeIssue]


# OVERALL SUMMARY

class AnalysisSummary(BaseModel):
    overall_strength: int = Field(
        ...,
        ge=0,
        le=100,
        description="Overall resume strength score"
    )
    headline: str = Field(
        ...,
        description="One-line assessment of the resume"
    )
    notes: Optional[str] = Field(
        default=None,
        description="Optional high-level commentary"
    )


# ROOT ANALYSIS SCHEMA RESULT

class AnalysisResult(BaseModel):
    """
    Canonical analysis output schema.\n
    Produced by the analysis orchestration stage.
    """

    summary: AnalysisSummary
    skill_evaluation: SkillEvaluation
    role_recommendations: RoleRecommendations
    critique: ResumeCritique