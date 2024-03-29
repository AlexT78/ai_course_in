import os
from dotenv import load_dotenv
import pinecone
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import Pinecone
from langchain.chains import RetrievalQA


load_dotenv()

#convert a text into chunk and convert each chunk into vector


def print_embedding_cost(texts):
    import tiktoken
    enc = tiktoken.encoding_for_model('text-embedding-ada-002') #will be decom soon, "text-embedding-3-small" or "text-embedding-3-large"
    total_tokens = sum([len(enc.encode(page.page_content)) for page in texts])
    print(f'total tokens: {total_tokens}')
    print(f'embedding cost in usd: {total_tokens / 1000 * 0.0004:.6f}')


with open('random_text.txt') as f:
    random_text = f.read()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 100, 
    chunk_overlap = 20,
    length_function = len
)

chunks = text_splitter.create_documents([random_text])

print(chunks[3].page_content)
print(f'now you have {len(chunks)} chunks')

print_embedding_cost(chunks)

embeddings = OpenAIEmbeddings()
# vector = embeddings.embed_query(chunks[0].page_content)
# print(vector)

#insert the embeddings into a pinecone index

# pc = pinecone.Pinecone()

# for i in pc.list_indexes().names():
#     print('deleting all indexes...')
#     pc.delete_index(i)
#     print("done")

# index_name = 'random-text'
# if index_name not in pc.list_indexes().names():
#     print(f"Creating index {index_name}")
#     pc.create_index(
#         name = index_name,
#         dimension = 1536, #default dimension for embedding
#         metric = "cosine", #algo used to calculate distance btw vector
#         spec = pinecone.PodSpec(
#             environment = "gcp-starter"
#         )
#     )
#     print("index created ")

#add the embedding chuncks in the db
# vector_store = Pinecone.from_documents(chunks, embeddings, index_name = index_name)

#load vector from existing index
vector_store = Pinecone.from_existing_index(index_name = "random-text", embedding = embeddings)


#we get the vectors who fit most the query 
query = "what is the story about ?"
result = vector_store.similarity_search(query)
print(result)

llm = ChatOpenAI(model ='gpt-3.5-turbo', temperature =1)

retriever = vector_store.as_retriever(search_type="similarity", search_kwargs ={"k":3})

chain = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever)
query = "do me a summarize in 3 sentences of the story "
answer = chain.run(query)
print(answer)