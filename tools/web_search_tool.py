from langchain.tools import tool

from langchain_community.tools import (
    DuckDuckGoSearchRun
)

search = DuckDuckGoSearchRun()

@tool
def web_search(query: str):

    """
    Search internet.
    """

    return search.run(query)