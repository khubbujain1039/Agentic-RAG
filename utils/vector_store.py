from langchain_chroma import Chroma

from utils.embeddings import (
    get_embedding_model
)

def get_vector_store():

    embeddings = get_embedding_model()

    return Chroma(
        collection_name="knowledge_base",
        embedding_function=embeddings,
        persist_directory=
        "data/vector_db/chroma_db"
    )