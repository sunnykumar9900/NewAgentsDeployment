from ..services.llm import llm
from ..tools.naukri_search import search_tool

SYSTEM_PROMPT = (
    "You are a Naukri.com job market research assistant. "
    "Use only the supplied Naukri search results; do not call or invent tools. "
    "Report the total job opening count only if it is explicitly shown in the "
    "supplied search-result content. Otherwise report 'Not available'. "
    "Never estimate or confuse total openings with the number of listings retrieved. "
    "Only include listings whose stated experience range accepts candidates "
    "with 9 or more years of experience; exclude listings requiring less than "
    "9 years or where the experience requirement is not available. "
    "Return these sections: "
    "1. Total openings displayed on Naukri. "
    "2. Number of individual listings retrieved before experience filtering. "
    "3. Job listing details with title, company, location, experience and URL. "
    "Do not invent missing details; label them 'Not available'."
)


def search_jobs(skills: str):
    skills = skills.strip()
    if not skills:
        raise ValueError("Skills must not be empty.")

    search_response = search_tool.invoke(
        {"query": f"{skills} jobs site:naukri.com"}
    )
    if "error" in search_response:
        raise RuntimeError(f"Tavily search failed: {search_response['error']}")

    results = search_response.get("results", [])
    listings = "\n\n".join(
        f"Title: {result.get('title', 'Not available')}\n"
        f"URL: {result.get('url', 'Not available')}\n"
        f"Content: {result.get('content', 'Not available')[:1200]}"
        for result in results
    )
    if not listings:
        listings = "No Naukri search listings were returned."

    response = llm.invoke(
        [
            ("system", SYSTEM_PROMPT),
            (
                "human",
                f"Skills: {skills}\n"
                f"Number of individual listings retrieved: {len(results)}\n\n"
                f"Tavily Naukri search results:\n{listings}",
            ),
        ]
    )

    return response.content