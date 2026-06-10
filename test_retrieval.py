# test_retrieval.py

from utils.vector_store import get_vector_store

vector_store = get_vector_store()

query = input("Ask: ")

docs = vector_store.similarity_search(
    query,
    k=3
)

for doc in docs:
    print("\n")
    print(doc.page_content)