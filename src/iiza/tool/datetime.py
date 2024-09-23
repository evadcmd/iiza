from datetime import datetime
from typing import Any


class Datetime:
    def __str__(self) -> str:
        return "Datetime"

    def __repr__(self) -> str:
        tool_description = 'A tool returns current datetime in "{YEAR}-{MONTH}-{DAY} {HOUR}:{MINUTE}:{SECOND}" format'
        input_format = "no input is required"
        return f"[tool-name]{str(self)} [tool-description] {tool_description} [input-format] {input_format}"

    async def __call__(self, *args: Any, **kwargs: Any) -> str:
        return datetime.now().strftime("%Y-%m-%d %a %H:%M:%S")
