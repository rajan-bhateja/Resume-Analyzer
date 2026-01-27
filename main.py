from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import ValidationError, EmailStr
import json

from contracts.api.analyze import AnalyzeRequest
from contracts.errors.error import ErrorContract, ErrorDetail
from contracts.events.sse import (
    RequestAcceptedEvent,
    ResumeParsedEvent,
    AnalysisStepCompletedEvent,
    ResumeSectionGeneratedEvent,
    AnalysisCompleteEvent,
)

from backend.utilities import (
    validate_resume_extension,
    validate_content_type,
    validate_file_size,
    generate_request_id,
    get_time_utc,
)

app = FastAPI(title="Resume Analyzer")


@app.get("/status")
async def get_status() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/analyze")
async def analyze_resume(
    email: EmailStr = Form(...),
    generate_modified_resume: bool = Form(False),
    focus: str | None = Form(None),
    resume: UploadFile = File(...)
):
    # CONTRACT VALIDATION
    try:
        analyze_request = AnalyzeRequest(
            email=email,
            generate_modified_resume=generate_modified_resume,
            focus=focus
        )
    except ValidationError as e:
        error = ErrorContract(
            code="VALIDATION_ERROR",
            message="Invalid request payload",
            recoverable=False,
            details=ErrorDetail(info=e.errors())
        )
        raise HTTPException(status_code=400, detail=error.model_dump())

    # FILE VALIDATIONS
    try:
        validate_resume_extension(resume.filename)
        validate_content_type(resume.content_type)

        contents = await resume.read()
        file_size_bytes = len(contents)
        validate_file_size(file_size_bytes)

        resume.file.seek(0)  # place the pointer back to the beginning

    except ValueError as e:
        error = ErrorContract(
            code="VALIDATION_ERROR",
            message=str(e),
            recoverable=False
        )
        raise HTTPException(status_code=400, detail=error.model_dump())

    # SSE LIFECYCLE
    request_id = generate_request_id()
    timestamp = get_time_utc()

    async def event_stream():
        # 1) request_accepted event
        evt = RequestAcceptedEvent(
            event="request_accepted",
            request_id=request_id
        )
        yield (
            f"event: {evt.event}\n"
            f"data: {json.dumps(evt.model_dump(exclude={'event'}))}\n\n"
        )

        # 2) resume_parsed event
        evt = ResumeParsedEvent(event="resume_parsed")
        yield (
            f"event: {evt.event}\n"
            f"data: {{}}\n\n"
        )

        # 3) analysis steps (skeleton) event
        for step in [
            "skills_extracted",
            "skills_evaluated",
            "resume_criticized",
            "roles_recommended",
        ]:
            evt = AnalysisStepCompletedEvent(
                event="analysis_step_completed",
                step=step       # noqa
            )
            yield (
                f"event: {evt.event}\n"
                f"data: {json.dumps({'step': step})}\n\n"
            )

        # 4) optional rewritten resume sections (skeleton) event
        if analyze_request.generate_modified_resume:
            for section in ["summary", "experience", "skills"]:
                evt = ResumeSectionGeneratedEvent(
                    event="resume_section_generated",
                    section=section,
                    content={}
                )
                yield (
                    f"event: {evt.event}\n"
                    f"data: {json.dumps({'section': section, 'content': {}})}\n\n"
                )

        # 5) analysis_complete event
        evt = AnalysisCompleteEvent(
            event="analysis_complete",
            analysis={},
            rewritten_resume={} if analyze_request.generate_modified_resume else None
        )
        yield (
            f"event: {evt.event}\n"
            f"data: {json.dumps(evt.model_dump(exclude={'event'}))}\n\n"
        )

    return StreamingResponse(
        event_stream(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
        },
    )
