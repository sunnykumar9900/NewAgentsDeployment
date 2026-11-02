import os
from pathlib import Path

from dotenv import load_dotenv
from langchain_tavily import TavilySearch

PROJECT_ROOT = Path(__file__).resolve().parents[3]
ENV_PATH = PROJECT_ROOT / "Config" / ".env"
load_dotenv(ENV_PATH)

if not os.getenv("TAVILY_API_KEY"):
    raise ValueError(f"TAVILY_API_KEY not found in {ENV_PATH}")

search_tool = TavilySearch(
    max_results=3,
    topic="general",
    search_depth="basic",
    include_domains=["naukri.com"],
    include_answer=False,
    include_raw_content=False,
)


if __name__ == "__main__":
    response = search_tool.invoke({
        "query": "Python Playwright jobs site:naukri.com"
    })

    print(response)