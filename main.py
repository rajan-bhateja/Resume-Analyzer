from fastapi import FastAPI, UploadFile, File

app = FastAPI(title="Resume Analyzer")


@app.get("/status")
async def get_status() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/analyze")
async def analyze_resume(email: str = File(...), resume: UploadFile = File(...)):
    # Read the filename
    filename = resume.filename

    # Read the content (optional, depending on your logic)
    # content = await resume.read()

    return {
        "email": email,
        "filename": filename,
        "content_type": resume.content_type
    }


@app.post("/refine")
def refine_resume():
    pass