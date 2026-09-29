from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI
from routers.chat import router as chat_router


app = FastAPI(title="EYA FastAPI Groq Workshop")

app.include_router(chat_router)


@app.get("/health")
def health() -> dict[str, str]:

    return {
        "status": "ok"
    }