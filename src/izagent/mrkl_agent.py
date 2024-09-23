"""Attempt to implement MRKL systems as described in arxiv.org/pdf/2205.00445.pdf."""

import logging

from izagent import mrkl_tpl
from izagent.llm import openai
from izagent.tool.datetime import Datetime
from izagent.tool.websearch import WebSearch

logger = logging.getLogger(__name__)

tools = [Datetime(), WebSearch()]

tool_map = {str(tool): tool for tool in tools}
tool_descriptions = "\n".join([f"{tool}: {repr(tool)}" for tool in tools])
tool_names = ", ".join([f"{tool}: {str(tool)}" for tool in tools])


selector = openai.Client(model=openai.Model.GPT3dot5Turbo)
answerer = openai.Client(model=openai.Model.GPT4)


async def induce(
    question: str,
) -> str:
    prompt = mrkl_tpl.TEMPLATE.format(
        tool_descriptions=tool_descriptions,
        tool_names=tool_names,
        input=question,
    )

    try:
        for _ in range(10):
            logger.info(f"{prompt=}")
            ans = await selector.completion(
                prompt,
                stop=mrkl_tpl.STOP_FLAGS,
            )
            logger.info(f"{ans=}")

            if m := mrkl_tpl.FINISH_REGEX.search(ans):
                # return res[m.end() :]
                # let the answerer summarize the information received and provide the final answer.
                if ans := await answerer.completion(prompt + ans[: m.end()]):
                    return ans
                else:
                    break
            elif m := mrkl_tpl.ACTION_REGEX.search(ans):
                tool_name, tool_input = m.group(1), m.group(2)
                logger.info(f"{tool_name=} {tool_input}")
                try:
                    observation = await tool_map[tool_name](tool_input)
                    logger.info(observation)
                except Exception as e:
                    logger.warning(
                        f"tool[{tool_name=} {tool_input=}] execution failed: {e}"
                    )
                    break
                prompt += ans + "Observation: " + observation + "\n"
            else:
                logger.warning(f"parse llm output failed: {ans}")
                break
    except Exception as e:
        logger.error(e)
    return await answerer.completion(question)
