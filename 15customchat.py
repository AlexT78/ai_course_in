#1.
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage
from langchain.chains import LLMChain
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, MessagesPlaceholder
from langchain.memory import ConversationBufferMemory, FileChatMessageHistory

load_dotenv()


llm = ChatOpenAI(model_name ="gpt-3.5-turbo", temperature = 1)

#2.initialize the chat memory object and the history object

history = FileChatMessageHistory('chat_history.json')
memory = ConversationBufferMemory(
    memory_key ="chat_history",
    chat_memory = history,
    return_messages=True #return message as list of memory instead of string
)


#3.
prompt = ChatPromptTemplate(
    input_variables = ["content"],
    messages = [
        SystemMessage(content =" respond only in french"),
        MessagesPlaceholder(variable_name="chat_history"), # where the memory will be stored
        HumanMessagePromptTemplate.from_template("{content}")

    ]
)


chain = LLMChain(
    llm=llm,
    prompt=prompt,
    memory=memory, 
    verbose=True
)

while True:
    content = input ("your prompt: ")
    if content in ["quit", "exit", "bye"]:
        print("goodbye")
        break
    response = chain.invoke({"content": content})
    print(response)
    print("-"*20)