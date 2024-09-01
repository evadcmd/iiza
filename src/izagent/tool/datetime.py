from datetime import datetime
from typing import Any


class Datetime:
    def __str__(self) -> str:
        return "Datetime"

    def __repr__(self) -> str:
        return 'A tool returns current datetime in "{YEAR}-{MONTH}-{DAY} {HOUR}:{MINUTE}:{SECOND}" format'

    async def __call__(self, *args: Any, **kwargs: Any) -> str:
        return datetime.now().strftime("%Y-%m-%d %a %H:%M:%S")
