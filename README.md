📄 Smart Document Q&A (RAG System)

An AI-powered document intelligence application that allows users to upload PDF files and ask questions about their content. The system retrieves relevant sections from the documents using semantic search and generates answers using a locally running language model.

This project demonstrates a Retrieval-Augmented Generation (RAG) pipeline implemented with modern AI tools.

🚀 Features

📂 Upload one or multiple PDF documents

🔎 Semantic document search using vector embeddings

🧠 AI-generated answers based only on document context

💬 Chat-style question answering interface

⚡ Persistent FAISS vector database for fast retrieval

🖥 Runs completely locally using Ollama and open-source models

🧠 How It Works

The system follows a Retrieval-Augmented Generation workflow:

User uploads PDF
        ↓
Document is split into text chunks
        ↓
Chunks are converted into vector embeddings
        ↓
Embeddings stored in FAISS vector database
        ↓
User asks a question
        ↓
Relevant chunks are retrieved
        ↓
LLM generates an answer based on retrieved context

This ensures responses are grounded in the document content rather than hallucinated.

🛠 Tech Stack
Component	Technology
Programming Language	Python
LLM Framework	LangChain
Vector Database	FAISS
Embeddings	HuggingFace (MPNet)
Local LLM	Ollama (Gemma)
Web Interface	Streamlit
📂 Project Structure
smart-document-qa-rag/
│
├── app.py                 # Streamlit UI application
├── rag_pipeline.py        # Document processing + RAG pipeline
├── requirements.txt       # Python dependencies
├── README.md
├── .gitignore
│
├── documents/             # Uploaded PDFs
└── vector_store/          # Stored FAISS indexes
⚙️ Installation

Clone the repository:

git clone https://github.com/YOUR_USERNAME/smart-document-qa-rag.git

Navigate into the project:

cd smart-document-qa-rag

Install dependencies:

pip install -r requirements.txt
▶️ Running the Application

Start the Streamlit interface:

streamlit run app.py

The web interface will open in your browser.

Upload a document and start asking questions.

💬 Example Questions

You can ask questions like:

What topics are discussed in this document?

How many chapters are in this book?

What does the document say about communication?

Summarize the conclusion.

📌 Future Improvements

Potential enhancements for the system:

Page number citations in answers

Hybrid search (semantic + keyword search)

Document summarization

Better UI with conversation memory

Deployment for public access

👨‍💻 Author

Aravind

First AI project exploring:

Retrieval-Augmented Generation

Local LLM applications

AI-powered document intelligence systems

⭐ Acknowledgement
This project was built as part of learning modern AI development workflows involving:

LLMs

Vector databases

Document retrieval systems