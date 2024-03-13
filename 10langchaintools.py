from dotenv import load_dotenv
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.tools import DuckDuckGoSearchResults
from langchain_community.utilities import DuckDuckGoSearchAPIWrapper
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
import re

load_dotenv()


# search=DuckDuckGoSearchRun()
# output=search.invoke("in one sentence, where live stephanie de monaco")
# print(output)
# print(search.name)
# print(search.description)


# search = DuckDuckGoSearchResults()
# output =search.run("freddie mercury and queen")
# print(output)

######
wrapper = DuckDuckGoSearchAPIWrapper(region="fr-fr", max_results=3,safesearch="moderate")
search = DuckDuckGoSearchResults(api_wrapper=wrapper, source="news")
output =search.run("montreal")
print(output)

pattern = r'snippet: (.*?), title: (.*?), link: (.*?)\],'
matches = re.findall(pattern, output, re.DOTALL)

for snippet, title, link in matches:
    print('-' *20)
    print(f'Snippet: {snippet}\nTitle: {title}\nLink: {link}\n')
######

api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=200)
wiki=WikipediaQueryRun(api_wrapper=api_wrapper)

output= wiki.invoke({"query": "llamaindex"})
print(output)

output= wiki.invoke({"query": "openai"})
print(output)
