from fastapi import APIRouter
from pydantic import BaseModel

from izagent import mrkl_agent
from izagent.router import API_V0
from izagent.tool.datetime import Datetime
from izagent.tool.websearch import WebSearch

router = APIRouter(prefix=API_V0, tags=[API_V0])


class Message(BaseModel):
    content: str


default_tools = [Datetime(), WebSearch()]


@router.post("")
async def inferer(msg: Message) -> str:
    return await mrkl_agent.induce(msg.content, tools=default_tools)
