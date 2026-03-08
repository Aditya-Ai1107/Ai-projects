from langchain_classic.chains import RetrievalQA
from langchain_classic.prompts import PromptTemplate
from langchain_community.llms import HuggingFacePipeline
from transformers import pipeline

def create_chatbot(vectorstore):

    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

    pipe = pipeline(
        "text-generation",
        model="google/flan-t5-base",
        max_new_tokens=256
    )
    llm = HuggingFacePipeline(pipeline=pipe)
    prompt_template = """
        I am a helpful assistant answering questions from a PDF document.
        Context:
        {context}
        
        Question:
        {question}
    """
    PROMPT = PromptTemplate(
        template=prompt_template,
        input_variables=["context", "question"]
    )
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",
        chain_type_kwargs={"prompt": PROMPT},
        return_source_documents=True
    )

    return qa_chain