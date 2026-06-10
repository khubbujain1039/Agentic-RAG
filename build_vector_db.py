from utils.document_loader import load_pdf

from utils.text_splitter import split_docs

from utils.vector_store import (
    get_vector_store
)

docs = load_pdf(
    "AI_notes.pdf"
)

chunks = split_docs(docs)

vector_store = get_vector_store()

vector_store.add_documents(chunks)

print("Vector DB Created")