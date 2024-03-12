from langchain.globals import set_llm_cache
from langchain_openai import OpenAI
from langchain.cache import InMemoryCache
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(model_name="gpt-3.5-turbo-instruct")

set_llm_cache(InMemoryCache())
prompt = "tell me a joke that a toddler can understand"
output = llm.invoke(prompt)

print(output)

llm.invoke(prompt)


#SQLlite caching
#from langchain.cache import SQLiteCache
#set_llm_cache(SQLiteCache(database_path=".langchain.db"))
#llm.invoke("tell me a joke") #first request
#llm.invoke("tell me a joke") #second request