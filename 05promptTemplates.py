from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv


load_dotenv()

template = '''You are an experienced virologist
Write a few sentence about the following virus "{virus}" in  {language}'''

prompt_template= PromptTemplate.from_template(template=template)

prompt = prompt_template.format(virus = "cold", language ="french")

llm = ChatOpenAI(model_name='gpt-3.5-turbo', temperature=0)
output = llm.invoke(prompt)
print(output.content)