# RAG-Based Chatbot 🤖

A Retrieval-Augmented Generation (RAG) chatbot built using Python, LangChain, FAISS, and HuggingFace embeddings.

The chatbot answers questions based on custom documents by retrieving relevant context from a vector database.

---

## Features

- Document based Question Answering
- FAISS Vector Database
- HuggingFace Embeddings
- Retrieval-Augmented Generation (RAG)
- Streamlit Chat UI

---

## Project Structure


RAG-based-chatbot/
│
├── app.py
├── create_vectorstore.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── data/
│   └── Cricket.pdf
│
├── src/
│   ├── chatbot.py
│   ├── retriever.py
│   ├── ingest.py
│   └── test.py
│
├── vectorstore/
│
└── notebooks/
    └── ingest.ipynb

---

## Installation

Clone the repository


git clone https://github.com/Aditya-Ai1107/rag-chatbot.git

cd rag-chatbot


Create virtual environment


python -m venv venv
venv\Scripts\activate


Install dependencies


pip install -r requirements.txt


---

## Create Vector Database


python create_vectorstore.py


---

## Run Chatbot


streamlit run app.py


---

## Tech Stack

- Python
- LangChain
- FAISS
- HuggingFace Embeddings
- Streamlit

---

## Future Improvements

- Multi-document support
- Chat history memory
- Deployment (HuggingFace / AWS)
- Better UI

---

## Author

Aditya Jagdale
