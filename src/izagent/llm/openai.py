import os
from enum import StrEnum

from openai import AsyncOpenAI
from pydantic import BaseModel

default_openai_client = AsyncOpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)


class Model(StrEnum):
    GPT3dot5 = "gpt-3.5"
    GPT3dot5Turbo = "gpt-3.5-turbo"
    GPT4 = "gpt-4"


class Client(BaseModel):
    openai_client: AsyncOpenAI = default_openai_client
    model: Model

    async def completion(self, msg: str, stop: str | list[str] | None = None) -> str:
        res = await self.openai_client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": msg,
                }
            ],
            temperature=0.9,
            stop=stop,
        )
        return res.choices[0].message.content or ""
