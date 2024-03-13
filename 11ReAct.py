#ReAct ==> combine reasoning (chain of thought prompting) and acting capabilities of llms
#it generate reasoning trace and task-specific actions

from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain import hub
from langchain.agents import Tool, AgentExecutor, initialize_agent, create_react_agent
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_community.tools import WikipediaQueryRun
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.tools import DuckDuckGoSearchResults
from langchain_experimental.tools.python.tool import PythonAstREPLTool
from langchain_openai import ChatOpenAI

load_dotenv()


llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

template ='''
Answer the following questions in french, as best you can.
Questions: {q}
'''

prompt_template = PromptTemplate.from_template(template)
prompt = hub.pull("hwchase17/react")

# print(type(prompt))
# print(prompt.input_variables)
# print(prompt.template)

#1.¨python REPL tool (for executing python code)
python_repl = PythonAstREPLTool()
python_repl_tool =Tool(
    name='python REPL',
    func=python_repl.run,
    description="useful when you need to use python to answer a question. you should input python code."

)

#2. wikipedia tool (for searching wiki)
api_wrapper = WikipediaAPIWrapper()
wikipedia=WikipediaQueryRun(api_wrapper=api_wrapper)
wikipedia_tool=Tool(
    name="wikipedia",
    func=wikipedia.run,
    description="useful for when you need to look up a topic, country or person on wikipedia"
)

#3.duckduckgo search tool(for general web searches)
search = DuckDuckGoSearchRun()
duckduckgo_tool=Tool(
    name="duckduckgo search",
    func=search.run,
    description="useful for when you need to perform an internet search to find information that another tool cannot provide"
)

#put the tools into a list
tools= [python_repl_tool,wikipedia_tool,duckduckgo_tool]

#combine the tools, agent and the prompt
agent = create_react_agent(llm, tools, prompt)

#set agent executor to run the agent
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
    handle_parsing_errors=True, #will handle eventual parsing error >agent more robust
    max_iterations=10 #maximum of steps from the agent
)

question = "generate the first 20 numbers in a the fibonacci series"

output = agent_executor.invoke({
    "input": prompt_template.format(q=question)
})

print(output["input"])
print(output["output"])

print("-"*20)
question = "who is the prime minister of france"
output = agent_executor.invoke({
    "input": prompt_template.format(q=question)
})

print("-"*20)
question = "tell me about napoleon bonapart early life"
output = agent_executor.invoke({
    "input": prompt_template.format(q=question)
})

print("-"*20)