from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain import PromptTemplate
from langchain.chains import LLMChain, SimpleSequentialChain

load_dotenv()

llm1=ChatOpenAI(model_name="gpt-3.5-turbo", temperature=.5)

prompt_template1 = PromptTemplate.from_template(
    template="you are experienced scientist and python programmer. write a function that implement the concept of {concept}"
)

chain1= LLMChain(llm=llm1, prompt=prompt_template1)

llm2=ChatOpenAI(model_name="gpt-3.5-turbo", temperature=1.2)

prompt_template2=PromptTemplate.from_template(
    template="given the python function {function}, describe it as detailed as possible"
)


chain2=LLMChain(llm=llm2,prompt=prompt_template2)

overall_chain = SimpleSequentialChain(chains=[chain1,chain2], verbose=True)
output=overall_chain.invoke("linear regression")
print(output["output"])