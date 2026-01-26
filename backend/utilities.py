import re
import uuid
from datetime import datetime, timezone


def validate_email(email: str) -> str:
    """Validates email address"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(pattern, email):
        raise ValueError(f"Invalid email address: {email}")

    return email


def validate_resume_extension(resume_filename: str) -> str:
    """Validates resume extension"""
    if not resume_filename.lower().endswith((".pdf", ".docx")):
        raise ValueError(
            f"Unsupported resume extension: {resume_filename}"
            f"\nSupported extensions: .pdf, .docx"
        )

    return resume_filename


def validate_content_type(content_type: str) -> str:
    """Validates content type"""
    if content_type.lower() not in ("application/pdf", "application/vnd.openxmlformats-officedocument.wordprocessingml.document"):
        raise ValueError(f"Invalid content type: {content_type}")

    return content_type


def validate_file_size(file_size_bytes: int, max_size_bytes: int = 5242880) -> int:
    """Validates file size in bytes."""
    if file_size_bytes > max_size_bytes:
        raise ValueError("File size cannot be greater than 5 MB")

    return file_size_bytes


def generate_request_id() -> str:
    """Generates a request id"""
    return str(uuid.uuid4())


def get_time_utc() -> str:
    """Gets current time in UTC"""
    return str(datetime.now(timezone.utc))


def normalize_string(string: str) -> str:
    """Normalizes string"""
    return string.strip().lower()
