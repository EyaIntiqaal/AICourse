# TOUTA FastAPI Groq Workshop

Short description
- A minimal FastAPI application that initializes environment variables at import time, registers a chat router, and exposes a simple health check endpoint.

Features
- Loads environment variables from a `.env` file at import time (using python-dotenv).
- Creates a FastAPI application with the title "TOUTA FastAPI Groq Workshop".
- Includes a chat router (imported from `routers.chat`) to register chat-related endpoints.
- Exposes a lightweight health check endpoint at `GET /health` that returns `{"status": "ok"}`.

Installation
1. Ensure you have Python 3.8+ installed.
2. Install required packages:
   - fastapi
   - python-dotenv
   - an ASGI server such as uvicorn (to run the app)

Example using pip:
pip install fastapi python-dotenv uvicorn

Usage
1. (Optional) Create a `.env` file in the project root if you need to provide environment variables. `load_dotenv()` is executed immediately at module import, so environment variables should be available before other modules import them.
2. Run the application with an ASGI server (example using uvicorn):
uvicorn main:app --host 0.0.0.0 --port 8000 --reload

3. Health check
- Request:
  GET /health
- Response:
  {
    "status": "ok"
  }

Project structure
- main.py
  - Entrypoint for the application.
  - Calls `load_dotenv()` immediately to populate environment variables.
  - Creates the FastAPI `app` with title "TOUTA FastAPI Groq Workshop".
  - Includes the `router` from `routers.chat`.
  - Defines a `GET /health` endpoint returning `{"status": "ok"}`.
- routers/chat.py
  - Referenced by main.py and expected to register chat-related endpoints.
  - (File contents not included in this repository snapshot; see that module for chat endpoint details.)

Notes
- Do not change the import/initialization order in main.py: `load_dotenv()` runs at import time so other modules can rely on environment variables.