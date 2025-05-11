# src/llm.py

import logging
from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv

# 1️⃣ Configure logger
logger = logging.getLogger("AgentLogger")
load_dotenv()
model = "models/gemini-2.0-flash"

try:
    llm = GoogleGenerativeAI(model=model)
    logger.info(f"Model {model} loaded successfully.")
except Exception as e:
    logger.exception(f"Failed to load the model {model}")
    print("⚠️ Failed to load the model. Please check your configuration.")
    print(f"Error occured : \n {e}")



def ask_llm(question: str, contexts: list[str]) -> str:
    """
    Uses DistilGPT2 to answer a question given retrieved contexts.
    """
    prompt = (
        "Use these excerpts to answer the question:\n\n"
        + "\n\n---\n\n".join(contexts)
        + f"\n\nQuestion: {question}\nAnswer:"
    )
    try:
        output = llm.invoke(prompt)
        return output
    except Exception as e:
        logger.exception("LLM call failed")
        return "⚠️ Sorry, I couldn’t generate an answer right now."
