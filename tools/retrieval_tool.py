from langchain.tools import tool

from utils.vector_store import (
    get_vector_store
)

vector_store = get_vector_store()

@tool
def retrieve_docs(query: str):

    """
    Search information from the uploaded PDF documents.

    Use this tool ONLY when the question is about
    information that may exist inside the indexed PDFs.

    Examples:
    - What is machine learning?
    - Explain neural networks.
    - Summarize chapter 3.
    """

    docs = vector_store.similarity_search(
        query,
        k=3
    )

    return "\n".join(
        doc.page_content
        for doc in docs
    )