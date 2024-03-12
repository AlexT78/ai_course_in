from dotenv import load_dotenv
from langchain_openai import ChatOpenAI


load_dotenv()

llm = ChatOpenAI()

output = llm.invoke('tell a joke about basketball', model= "gpt-4-turbo-preview") #will use gtp4 turbo, if no model, will use "gtp-3.5-turbo"
print(output.content)
