import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema import(
    SystemMessage, #the behavior AI
    AIMessage, #the AI msg
    HumanMessage #user msg
)

load_dotenv()

llm = ChatOpenAI()

#system is the behavior of the ai
#user is the prompt/question to ask
#assistant is the answer to the user prompt

messages = [
    SystemMessage(content="you are physicit and respond only in French"),
    HumanMessage(content="Explain quantum mechanics in one sentence")
]


output = llm.invoke(messages)
print(output.content)
