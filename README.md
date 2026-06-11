# Agentic RAG Research Assistant

## Overview

Agentic RAG Research Assistant is an AI-powered system that combines Retrieval-Augmented Generation (RAG) with tool-based decision making. The application can answer questions from uploaded PDF documents, perform mathematical calculations, search the web for external information, and summarize content.

The project uses ChromaDB as a vector database, HuggingFace embeddings for semantic search, and Ollama as the local Large Language Model (LLM).

---

## Features

* PDF document ingestion
* Automatic text chunking
* Embedding generation using HuggingFace models
* ChromaDB vector storage
* Semantic document retrieval
* Web search integration
* Mathematical calculations
* Text summarization
* Local LLM inference using Ollama
* Agent-based tool selection

---

## Project Architecture

User Query
↓
Research Agent
↓
Tool Selection
├── Retrieval Tool
├── Web Search Tool
├── Calculator Tool
└── Summarizer Tool
↓
Response Generation

---

## Folder Structure

Agentic-RAG/

├── app.py

├── build_vector_db.py

├── test_retrieval.py

├── requirements.txt

├── data/

│   └── documents/

│       └── mypdf.pdf

├── vector_db/

├── agents/

│   └── research_agent.py

├── tools/

│   ├── retrieval_tool.py

│   ├── web_search_tool.py

│   ├── calculator_tool.py

│   └── summarizer_tool.py

└── utils/

```
├── document_loader.py

├── text_splitter.py

├── embeddings.py

└── vector_store.py
```

---

## Technologies Used

### AI & LLM

* Ollama
* Qwen2.5 7B / Llama3
* LangChain

### Vector Database

* ChromaDB

### Embeddings

* HuggingFace Sentence Transformers

### Document Processing

* PyPDFLoader
* RecursiveCharacterTextSplitter

### Search

* DuckDuckGo Search

---

## Installation

### Clone Repository

git clone <repository_url>

cd Agentic-RAG

### Create Virtual Environment

python -m venv venv

### Activate Environment

Windows:

venv\Scripts\activate

Linux/Mac:

source venv/bin/activate

### Install Dependencies

pip install -r requirements.txt

---

## Install Ollama

Download and install Ollama:

https://ollama.com

Pull a model:

ollama pull qwen2.5:7b

Verify:

ollama list

---

## Add PDF Documents

Place your PDF inside:

data/documents/

Example:

data/documents/mypdf.pdf

---

## Build Vector Database

Run:

python build_vector_db.py

This process:

1. Loads the PDF
2. Splits text into chunks
3. Generates embeddings
4. Stores vectors in ChromaDB

Expected Output:

Vector DB Created

---

## Run Retrieval Test

Run:

python test_retrieval.py

Purpose:

* Tests only the retrieval pipeline
* Verifies vector search quality
* Useful for debugging

---

## Run Application

Run:

python app.py

Example:

Ask Question: What is Machine Learning?

Answer:
Machine Learning is a branch of Artificial Intelligence...

---

## Tool Descriptions

### Retrieval Tool

Searches relevant chunks from ChromaDB using semantic similarity search.

### Web Search Tool

Retrieves external information using DuckDuckGo Search.

### Calculator Tool

Performs mathematical calculations.

Examples:

1+2

25*40

100/4

### Summarizer Tool

Generates concise summaries from large text.

---

## Workflow

### Knowledge Ingestion

PDF
↓
Document Loader
↓
Text Splitter
↓
Embeddings
↓
ChromaDB

### Query Processing

User Query
↓
Agent
↓
Select Tool
↓
Retrieve Information
↓
Generate Response

---

## Future Improvements

* Multi-document support
* Chat memory
* Conversation history
* Streamlit UI
* Voice interaction
* Multi-agent architecture
* Hybrid retrieval
* Citation support

---

## Learning Outcomes

This project demonstrates:

* Retrieval-Augmented Generation (RAG)
* Vector Databases
* Embeddings
* ChromaDB
* LangChain
* Agentic AI
* Tool Calling
* Local LLM Deployment
* Semantic Search

---

## Author

Khushboo Jain

AI / Machine Learning Project

Agentic RAG Research Assistant
