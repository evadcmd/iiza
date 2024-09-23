import os
from enum import StrEnum

from openai import AsyncOpenAI

default_openai_client = AsyncOpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)


class Model(StrEnum):
    GPT3dot5Turbo = "gpt-3.5-turbo-1106"
    GPT4 = "gpt-4"


class Client:
    def __init__(self, model: Model):
        super().__init__()
        self.openai_client: AsyncOpenAI = default_openai_client
        self.model: Model = model

    async def completion(self, msg: str, stop: str | list[str] | None = None) -> str:
        res = await self.openai_client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": msg,
                }
            ],
            temperature=0.2,
            stop=stop,
        )
        return res.choices[0].message.content or ""
