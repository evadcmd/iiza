from enum import StrEnum

from openai import AsyncOpenAI
from pydantic import BaseModel


class Model(StrEnum):
    GPT3dot5 = "gpt-3.5"
    GPT3dot5Turbo = "gpt-3.5-turbo"
    GPT4 = "gpt-4"


class Client(BaseModel):
    openai: AsyncOpenAI
    model: Model

    async def completion(self, msg: str) -> str:
        return await openai.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "user",
                    "content": msg,
                }
            ],
            temperature=0.9,
        )
