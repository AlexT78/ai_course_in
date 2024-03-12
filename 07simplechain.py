from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(temperature=.5)

template = '''You are an experienced virologist
Write a few sentence about the following virus "{virus}" in  {language}'''
prompt_template = PromptTemplate.from_template(template=template)

chain = LLMChain(
    llm=llm,
    prompt=prompt_template,
    verbose=True #add more info
)

output=chain.invoke({'virus': 'cold', 'language': 'French'})
print(output['text'])


######
template02 = 'what is the capitol of {country}. list the top 3 place to visit. use bullet points'
prompt_template02=PromptTemplate.from_template(template=template02)

chain =LLMChain(
    llm=llm,
    prompt=prompt_template02,
    verbose=True

)
country = input("enter country: ")
output02 = chain.invoke(country)
print(output02["text"])