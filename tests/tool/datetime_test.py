import pytest

from izagent.tool.datetime import Datetime


@pytest.mark.asyncio
async def test_datetime():
    d = Datetime()
    print(await d("x"))
