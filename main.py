"""
Main application entrypoint for the TOUTA FastAPI Groq Workshop.

This module initializes the environment, creates the FastAPI application,
registers routers, and exposes a simple health check endpoint.

Do not change the order of imports or initialization side-effects: load_dotenv()
is intentionally executed immediately to populate environment variables used
elsewhere in the application.
"""

from dotenv import load_dotenv

# Load environment variables from a .env file into the process environment.
# This is executed at import time so subsequent imports can rely on env vars.
load_dotenv()

from fastapi import FastAPI
from routers.chat import router as chat_router


# Create the main FastAPI application instance. The title is used in the
# automatic API documentation (OpenAPI / Swagger UI).
app = FastAPI(title="TOUTA FastAPI Groq Workshop")

# Include the chat router which registers chat-related endpoints on the app.
app.include_router(chat_router)


@app.get("/health")
def health() -> dict[str, str]:
    """
    Health check endpoint.

    Returns a simple JSON object indicating the service status. This endpoint is
    useful for load balancers, uptime monitoring, and quick sanity checks.

    Returns:
        dict[str, str]: A mapping containing the status key with value "ok".
    """
    # Return a simple status payload. Keep the structure minimal to ensure the
    # endpoint is lightweight and reliable.
    return {
        "status": "ok"
    }