import logging
from urllib.parse import quote

import aiohttp
from pydantic import BaseModel

from qna.settings import settings

logger = logging.getLogger(__name__)


class Error(BaseModel):
    domain: str
    message: str


class Errors(BaseModel):
    errors: list[Error]


class Item(BaseModel):
    title: str
    link: str
    snippet: str


class Resp(BaseModel):
    items: list[Item]
    error: Errors | None


class WebSearch:
    def __init__(self):
        self.url = (
            settings.googlesearch.base_url.unicode_string() + "?key={}&cx={}&safe={}"
        )
        self.api_key = settings.googlesearch.api_key
        self.cse_id = settings.googlesearch.cse_id
        self.session = aiohttp.ClientSession()
        self.quote_filter = {ord(i): None for i in "'\""}

    def __str__(self) -> str:
        return "WebSearch"

    def __repr__(self) -> str:
        return "A tool for obtaining information form the internet"

    async def __call__(self, query: str, *, safe: bool = True) -> str:
        logger.info(f"{query=}")
        url = self.url.format(
            self.api_key,
            self.cse_id,
            quote(query.translate(self.quote_filter)),
            "active" if safe else "off",
        )
        async with self.session.get(url) as resp:
            res = Resp(**(await resp.json()))
            if res.error:
                raise Exception(", ".join(err.message for err in res.error.errors))
            return "    ".join(
                [
                    f"({idx+1}) {item.title} {item.snippet} {item.link}"
                    for idx, item in enumerate(res.items[:7])
                ]
            )
