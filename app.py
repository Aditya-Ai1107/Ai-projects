import streamlit as st
from src.retriever import load_vector_store
from src.chatbot import create_chatbot

st.title(" 🔗 RAG-Based PDF Chatbot 💻 ")

vectorstore = load_vector_store()
qa_chain = create_chatbot(vectorstore)

query = st.text_input("Ask a question from your PDFs")

if query:

    response = qa_chain.invoke({"query": query})

    answer = response.get("result", "").strip()

    # If model returns empty answer
    if not answer:
        answer = "The answer could not be generated, but relevant information was found in the document."

    st.markdown("### Answer👉📝")
    st.write(answer)

    st.markdown("### Source 📚")

    shown_pages = set()

    for doc in response["source_documents"]:
        page = doc.metadata["page"]

        if page not in shown_pages:
            st.write(f"- Page {page}")
            shown_pages.add(page)