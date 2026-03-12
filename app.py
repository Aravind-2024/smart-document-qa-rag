import streamlit as st
import os
from rag_pipeline import load_and_split_pdf, create_vector_store, build_rag_chain

st.set_page_config(
    page_title="Document Intelligence Assistant",
    page_icon="📄",
    layout="wide"
)

st.title("📄 Document Intelligence Assistant")

st.sidebar.header("Upload Documents")

uploaded_files = st.sidebar.file_uploader(
    "Upload PDF files",
    type=["pdf"],
    accept_multiple_files=True
)

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if uploaded_files:

    os.makedirs("documents", exist_ok=True)

    for file in uploaded_files:

        file_path = os.path.join("documents", file.name)

        with open(file_path, "wb") as f:
            f.write(file.getbuffer())

        doc_name = file.name.replace(".pdf", "")

        with st.spinner(f"Processing {file.name}..."):

            chunks = load_and_split_pdf(file_path)
            vector_store = create_vector_store(chunks, doc_name)
            llm, retriever = build_rag_chain(vector_store)

        st.session_state.retriever = retriever
        st.session_state.llm = llm

    st.sidebar.success("Documents processed successfully")

st.divider()

for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.write(message["content"])

query = st.chat_input("Ask a question about your documents")

if query:

    st.session_state.chat_history.append(
        {"role": "user", "content": query}
    )

    with st.chat_message("user"):
        st.write(query)

    retriever = st.session_state.retriever
    llm = st.session_state.llm

    docs = retriever.invoke(query)

    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = f"""
Answer the question using ONLY the context below.
If the answer is not present, say you cannot find it.

Context:
{context}

Question:
{query}

Answer:
"""

    response = llm.invoke(prompt)

    with st.chat_message("assistant"):
        st.write(response)

    st.session_state.chat_history.append(
        {"role": "assistant", "content": response}
    )