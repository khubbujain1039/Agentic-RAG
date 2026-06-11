from langchain.tools import tool

from langchain_community.tools import (
    DuckDuckGoSearchRun
)

search = DuckDuckGoSearchRun()

@tool
def web_search(query: str):

    """
    Search the internet for current or external information.

    Use this tool when:
    - Latest news
    - Current events
    - Information not available in PDFs

    Examples:
    - Latest GPT model
    - Who won IPL 2026?
    """

    return search.run(query)