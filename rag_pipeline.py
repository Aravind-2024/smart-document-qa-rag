import os
import warnings

warnings.filterwarnings("ignore")

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_ollama import OllamaLLM


def load_and_split_pdf(pdf_path):

    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=600,
        chunk_overlap=200
    )

    chunks = splitter.split_documents(documents)

    return chunks


def create_vector_store(chunks, doc_name):

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-mpnet-base-v2"
    )

    index_path = f"vector_store/{doc_name}"

    if os.path.exists(index_path):

        vector_store = FAISS.load_local(
            index_path,
            embeddings,
            allow_dangerous_deserialization=True
        )

    else:

        vector_store = FAISS.from_documents(
            chunks,
            embeddings
        )

        vector_store.save_local(index_path)

    return vector_store


def build_rag_chain(vector_store):

    llm = OllamaLLM(model="gemma3:4b")

    retriever = vector_store.as_retriever(
        search_type="mmr",
        search_kwargs={
            "k": 8,
            "fetch_k": 20
        }
    )

    return llm, retriever