from langchain_google_genai import GoogleGenerativeAI
from langchain.agents import initialize_agent, AgentType
from tools import calculator, rag
import os
from logger import logger
from dotenv import load_dotenv
load_dotenv()


model = "models/gemini-2.0-flash"
try:
    llm = GoogleGenerativeAI(model=model)
except Exception as e:
    logger.exception("Failed to load the model : {model}")
    print(f"Error occurred: {e}")

tools = [calculator, rag]

agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
)

def run_agent(query: str) -> str:
    logger.info(f"Received query: {query}")
    response_dict = agent.invoke({"input": query})
    logger.info(f"Raw agent response: {response_dict}")

    final_answer = response_dict.get("output", "Error: Could not retrieve final answer.")
    logger.info(f"Extracted final answer: {final_answer}")
    return final_answer
