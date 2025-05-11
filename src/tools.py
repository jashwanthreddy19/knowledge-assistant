import math
import re
from langchain.tools import Tool
from embed_index import get_relevant_chunks
from llm import ask_llm 
from logger import logger


# Simple safe‐eval for basic math
def calculator_tool(query: str) -> str:
    # extract digits and operators only
    logger.info("Using calculator tool.")
    expr = re.sub(r"[^0-9\.\+\-\*\/\(\) ]", "", query)
    try:
        result = eval(expr, {"__builtins__": {}}, math.__dict__)
        return str(result)
    except Exception as e:
        return f"Error: {e}"

def rag_tool(query: str) -> str:
    logger.info("Routing to RAG tool.")
    chunks = get_relevant_chunks(query)
    return ask_llm(query, chunks)

calculator = Tool(
    name="Calculator",
    func=calculator_tool,
    description="Useful for when you need to answer questions about math. Use this tool to perform calculations. Input should be a valid mathematical expression. This tool will return the numerical result of the calculation, which you should then provide as the final answer."
)

rag_tool_description = (
    "Use this tool to find information about a specific topic or to answer the user's question. "
    "Input should be the specific question or topic you need information about. "
    "This tool will return relevant text. "
    "CRITICAL INSTRUCTION: After you receive an 'Observation' from this tool, your very next 'Thought' MUST "
    "be to analyze if this 'Observation' directly and sufficiently answers the user's ORIGINAL question. "
    "If the 'Observation' provides the answer, your next step MUST be 'Final Answer:'. "
    "Do NOT re-ask the original question or call this tool again with the same input if the 'Observation' "
    "already contains the necessary information. Only use this tool again if you need DIFFERENT or "
    "MORE SPECIFIC information to answer the ORIGINAL question."
)

rag = Tool(
    name="RAG",
    func=rag_tool,
    description=rag_tool_description
)