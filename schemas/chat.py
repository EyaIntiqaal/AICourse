from pydantic import BaseModel


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    answer: str
    input_tokens: int
    output_tokens: int
    total_tokens: int