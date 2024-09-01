"""Attempt to implement MRKL systems as described in arxiv.org/pdf/2205.00445.pdf."""

import logging
from typing import Awaitable, Callable, Sequence

from izagent import mrkl
from izagent.llm import openai

logger = logging.getLogger(__name__)


selector = openai.Client(model=openai.Model.GPT3dot5)
answerer = openai.Client(model=openai.Model.GPT4)


async def induce(
    question: str,
    tools: Sequence[Callable[[str], Awaitable[str]]] | None = None,
) -> str:
    if not tools:
        return await answerer.completion(question)

    tool_map: dict[str, Callable[[str], Awaitable[str]]] = {
        str(tool): tool for tool in tools
    }

    tool_descriptions = "\n".join([f"{tool}: {repr(tool)}" for tool in tools])
    tool_names = ", ".join([f"{tool}: {str(tool)}" for tool in tools])

    content = mrkl.TEMPLATE.format(
        tool_descriptions=tool_descriptions,
        tool_names=tool_names,
        input=question,
    )

    try:
        for _ in range(10):
            res = await selector.completion(
                content,
                stop=mrkl.STOP_FLAGS,
            )

            if m := mrkl.FINISH_REGEX.search(res):
                return res[m.end() :]
                # if res := await conclusion_chain.apredict(
                #     content=content + res[:m.end()]
                # ):
                #     return res
                # else:
                #     break
            elif m := mrkl.ACTION_REGEX.search(res):
                tool_name, tool_input = m.group(1), m.group(2)
                try:
                    observation = await tool_map[tool_name](tool_input)
                except Exception as e:
                    logger.warning(
                        f"tool[{tool_name=} {tool_input=}] execution failed: {e}"
                    )
                    break
                content += res + "Observation: " + observation + "\n"
            else:
                logger.warning(f"parse llm output failed: {res}")
                break
    except Exception as e:
        logger.error(e)
    return await answerer.completion(question)
