import os

from fastapi import HTTPException, Security
from fastapi.security import APIKeyHeader


api_key_header = APIKeyHeader(
    name="Authorization",
    auto_error=False
)


def verify_api_key(
    api_key: str | None = Security(api_key_header)
) -> str:

    expected_api_key = os.getenv("API_KEY")

    if not expected_api_key:
        raise RuntimeError("API_KEY is not configured")

    if api_key != expected_api_key:
        raise HTTPException(
            status_code=401,
            detail="Invalid or missing API key"
        )

    return api_key