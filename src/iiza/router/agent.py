from fastapi import APIRouter
from pydantic import BaseModel

from iiza import mrkl_agent
from iiza.router import API_V0

router = APIRouter(prefix=API_V0, tags=[API_V0])


class Message(BaseModel):
    content: str


@router.post("/mrkl")
async def infer(msg: Message) -> str:
    return await mrkl_agent.induce(msg.content)


# for testing
from iiza.llm import openai


@router.post("/plain")
async def completion(msg: Message) -> str:
    client = openai.Client(model=openai.Model.GPT4)
    return await client.completion(msg.content)
