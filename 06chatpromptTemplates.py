from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, SystemMessagePromptTemplate
from langchain_core.messages import SystemMessage
from langchain_openai import ChatOpenAI

from dotenv import load_dotenv


load_dotenv()

llm = ChatOpenAI()


chat_template = ChatPromptTemplate.from_messages(
    [
        SystemMessage(content="you responds only in json format"),
        HumanMessagePromptTemplate.from_template("top {n} countries in {area} by population")
    ]
)

messages = chat_template.format_messages(n="10", area = " america")
print(messages)

output = llm.invoke(messages)
print(output.content)

