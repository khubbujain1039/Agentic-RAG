from langchain.tools import tool

from utils.vector_store import (
    get_vector_store
)

vector_store = get_vector_store()

@tool
def retrieve_docs(query: str):

    """
    Retrieve relevant documents.
    """

    docs = vector_store.similarity_search(
        query,
        k=3
    )

    return "\n".join(
        doc.page_content
        for doc in docs
    )