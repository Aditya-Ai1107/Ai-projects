from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_classic.schema import Document

# Load PDF
loader = PyPDFLoader("data/Cricket.pdf")
pages = loader.load()

documents = []

# Add page metadata
for page in pages:
    documents.append(
        Document(
            page_content=page.page_content,
            metadata={"page": page.metadata["page"] + 1}
        )
    )

# Split text into smaller chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=400,
    chunk_overlap=50
)

docs = text_splitter.split_documents(documents)

# Load embedding model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Create FAISS index
vectorstore = FAISS.from_documents(docs, embeddings)

# Save vector database
vectorstore.save_local("vectorstore")

print("Vector store created successfully!")