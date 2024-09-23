import re

TEMPLATE = """You function as a versatile assistant. Endeavor to answer the subsequent queries to the best of your ability. You passes access to the tools specified below:

{tool_descriptions}

Rigorously adhere to the ensuing format to deduce the "Final Answer":

Question: The input query that necessitates your response
Thought: You should always think about what to do
Action: The action to take, should be one of [{tool_names}]
Action Input: The input of the chosen action
Observation: Record the outcome stemming from the executed action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I have now acquired the definitive solution
Final Answer: The ultimate response to the original input question

* Always strive to provide an answer within the "Final Answer" text section or fill in the text within "Thought/Action/Action Input" as an alternative.
* Summarize your findings based on the observed facts to the greatest extent possible.
* If you derive information from online resources, ALWAYS INCLUDE THE RELEVANT URLs as references at the end of your "Final Answer".
* You should give the answer containing information as much as possible based on the fact in Japanese in the Final Answer block. eg: ...Final Answer: "${{ use japanese here }}".

Question: {input}
Thought:"""

STOP_FLAGS = ["Observation"]
FINISH_REGEX = re.compile(r"Final Answer\s*:\s*")
ACTION_REGEX = re.compile(r"Action\s*:\s*(.*)\s*Action\s*Input\s*:\s*(.*)")
