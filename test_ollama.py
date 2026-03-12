from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="gemma3:4b")

response = llm.invoke("Explain what a vector database is in 3 lines.")
print(response) 