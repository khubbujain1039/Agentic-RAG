from langchain.tools import tool

@tool
def summarize(text: str):

    """
    Summarize content.
    """

    return text[:1000]