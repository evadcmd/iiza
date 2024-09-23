import pytest

from iiza.tool.websearch import WebSearch


@pytest.mark.asyncio
async def test_websearch():
    ws = WebSearch()
    print(await ws(query="typhoon"))
