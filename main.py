from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from backend.utilities import (
    validate_email,
    validate_resume_extension,
    validate_content_type,
    # validate_file_size,
    generate_request_id,
    get_time_utc
)


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
        # contents = await resume.read()
        # file_size_bytes = len(contents)
        # validated_file_size = validate_file_size(file_size_bytes)
        validated_email = validate_email(email)
        validated_filename = validate_resume_extension(resume.filename)
        validated_content_type = validate_content_type(resume.content_type)
        uuid_str = generate_request_id()

        # resume.file.seek(0)     # Place the pointer to the beginning of the file

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    return {
        "email": validated_email,
        "filename": validated_filename,
        "content_type": validated_content_type,
        # "file_size": validated_file_size,
        "uuid": uuid_str,
        "timestamp": get_time_utc()
    }
