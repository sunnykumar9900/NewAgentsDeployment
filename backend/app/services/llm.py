
import os
from pathlib import Path
from dotenv import load_dotenv
from langchain_groq import ChatGroq

# Load environment variables from project config folder
PROJECT_ROOT = Path(__file__).resolve().parents[3]
ENV_PATH = PROJECT_ROOT / "config" / ".env"

load_dotenv(ENV_PATH)

# Read Groq API key
groq_api_key = os.getenv("GROQ_API_KEY")

if not groq_api_key:
    raise ValueError("GROQ_API_KEY not found in config/.env")

# Initialize Groq LLM
llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0
)


if __name__ == "__main__":
    response = llm.invoke("Explain what a ReAct AI agent is in two sentences.")
    print(response.content)
