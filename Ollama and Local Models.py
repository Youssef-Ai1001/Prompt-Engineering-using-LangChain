# !pip install ollama
# !pip install -U langchain-ollama

# !ollama list              # in CLI

# from langchain_community.llms import Ollama
# from langchain_community.chat_models import ChatOllama

from langchain_ollama import OllamaLLM, ChatOllama

# إنشاء الـ LLM object
llm = OllamaLLM(model="llama3:latest")

# تجربة بسيطة
response = llm.invoke("Explain what LangChain is in one sentence.")
print(response)