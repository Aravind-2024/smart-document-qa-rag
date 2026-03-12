from rag_pipeline import load_and_split_pdf, create_or_load_vector_store, build_rag_chain
import warnings
warnings.filterwarnings("ignore")

# Step 1: Process document
chunks = load_and_split_pdf("sample.pdf")
vector_store = create_or_load_vector_store(chunks)

# Step 2: Build retriever + model
llm, retriever = build_rag_chain(vector_store)

print("\nDocument ready. You can now ask questions.")
print("Type 'exit' to stop.\n")

while True:

    query = input("Ask a question: ")

    if query.lower() == "exit":
        break

    # Retrieve relevant chunks
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

    print("\nAnswer:\n")
    print(response)
    print("\n--------------------------\n")