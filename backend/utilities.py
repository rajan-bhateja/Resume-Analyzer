import re

def validate_email(email: str) -> str:
    """Validates email address"""

    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(pattern, email):
        raise ValueError(f"Invalid email address: {email}")

    return email


def validate_resume_extension(resume_filename: str) -> str:
    """Validates resume extension"""

    if not resume_filename.lower().endswith((".pdf", ".docx")):
        raise TypeError(
            f"Unsupported resume extension: {resume_filename}"
            f"\nSupported extensions: .pdf, .docx"
        )

    return resume_filename