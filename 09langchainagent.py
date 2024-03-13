from langchain_experimental.utilities import PythonREPL
from langchain_experimental.agents.agent_toolkits import create_python_agent
from langchain_experimental.tools.python.tool import PythonREPLTool
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

# python_repl= PythonREPL()
# print(python_repl.run("print([n for n in range(1,100) if n % 13 ==0])"))

llm =ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

agent_executor = create_python_agent(
    llm=llm,
    tool=PythonREPLTool(),
    verbose=True,
    handle_parsing_errors=True
)

#agent_executor.invoke("calculate the square root of the factorial of 12 and display it with 4 decimal points")

agent_executor.invoke("calculate the answer of 5.1 ** 7.3")

