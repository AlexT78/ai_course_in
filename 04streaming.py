from langchain.globals import set_llm_cache
from langchain_openai import OpenAI, ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI()

prompt = "write a small rock song about a mouse and the moon"

#usual way =-> going to print everything at the end
# print(llm.invoke(prompt).content)

#streaming.
for chunk in llm.stream(prompt):
    print(chunk.content, end="", flush=True)