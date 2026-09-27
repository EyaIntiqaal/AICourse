import os

from fastapi import APIRouter, Depends, HTTPException
from openai import OpenAI

from dependencies.auth import verify_api_key
from schemas.chat import ChatRequest, ChatResponse


router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)


groq_api_key = os.getenv("GROQ_API_KEY")

if not groq_api_key:
    raise RuntimeError("GROQ_API_KEY is not configured")


client = OpenAI(
    api_key=groq_api_key,
    base_url="https://api.groq.com/openai/v1"
)


@router.post("", response_model=ChatResponse)
def chat(request: ChatRequest, _: str = Depends(verify_api_key)) -> ChatResponse:
    try:
        response = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[
                {
                    "role": "user",
                    "content": request.message
                }
            ],
            max_tokens=300
        )

        usage = response.usage

        return ChatResponse(
            answer=response.choices[0].message.content,
            input_tokens=usage.prompt_tokens,
            output_tokens=usage.completion_tokens,
            total_tokens=usage.total_tokens
        )

    except Exception as error:

        raise HTTPException(
            status_code=500,
            detail=f"LLM request failed: {error}"
        )