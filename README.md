# TOUTA FastAPI Groq Workshop

Short description
-----------------
This repository contains the main application entrypoint for the TOUTA FastAPI Groq Workshop. The application loads environment variables from a `.env` file at import time, creates a FastAPI app instance (titled "TOUTA FastAPI Groq Workshop"), and includes a router from `routers.chat`. It also exposes a minimal health check endpoint.

Features
--------
- Loads environment variables from a `.env` file at import time using python-dotenv.
- Creates a FastAPI application with the title "TOUTA FastAPI Groq Workshop".
- Includes a modular router from `routers.chat`.
- Provides a lightweight health check endpoint at `GET /health` returning `{"status": "ok"}`.

Installation
------------
Dependencies inferred from the imports in the code:
- python-dotenv
- fastapi
- an ASGI server (e.g., uvicorn) to run the FastAPI app

Example installation using pip:
- pip install python-dotenv fastapi uvicorn

Usage
-----
1. Ensure any required environment variables are provided (for example via a `.env` file). The application calls load_dotenv() at import time, so environment variables are available to other modules on import.
2. Start the application with an ASGI server. For example, using uvicorn:
   uvicorn main:app --reload
3. Health check:
   - Request: GET /health
   - Response: JSON object with a single key `status` and value `"ok"`, e.g.:
     {"status": "ok"}

Project structure
-----------------
Files and modules referenced by the code:
- main.py
  - Application entrypoint
  - Calls load_dotenv() immediately on import
  - Creates FastAPI(title="TOUTA FastAPI Groq Workshop")
  - Includes router from `routers.chat`
  - Defines `GET /health` that returns `{"status": "ok"}`
- routers/chat.py
  - Imported as `from routers.chat import router as chat_router`
  - Expected to expose a FastAPI router object named `router`

Optional/auxiliary:
- .env (optional): environment variables loaded by load_dotenv()

Notes
-----
- The README only describes what is visible in the provided source: main application initialization, environment loading, router inclusion, and the health endpoint. Details of the chat router and other modules are not described because their source is not shown here.