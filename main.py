from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from backend.utilities import validate_email, validate_resume_extension

app = FastAPI(title="Resume Analyzer")


@app.get("/status")
async def get_status() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/analyze")
async def analyze_resume(
    email: str = Form(...),
    resume: UploadFile = File(...)
):
    try:
        validated_email = validate_email(email)
        validated_filename = validate_resume_extension(resume.filename)

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    return {
        "email": validated_email,
        "filename": validated_filename,
        "content_type": resume.content_type
    }
