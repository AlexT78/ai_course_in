import os
from dotenv import load_dotenv
from pinecone import Pinecone
from pinecone import PodSpec
import random


load_dotenv()

pc = Pinecone()

# print(pc.list_indexes())
# print(pc.list_indexes()[0]['name']) # get the name of the index on position => sample-movies if the sample db from pinecone
# print(pc.describe_index("sample-movies")) #list index "sample-movies"
# print(pc.list_indexes().names()) #list all indexes
'''
{'indexes': [{'dimension': 1536,
              'host': 'sample-movies-4073038.svc.gcp-starter.pinecone.io',
              'metric': 'cosine',
              'name': 'sample-movies',
              'spec': {'pod': {'environment': 'gcp-starter',
                               'pod_type': 'starter',
                               'pods': 1,
                               'replicas': 1,
                               'shards': 1}},
              'status': {'ready': True, 'state': 'Ready'}}]}
'''
index_name = "langchain"

#create index
if index_name not in pc.list_indexes().names():
    print(f"Creating index {index_name}")
    pc.create_index(
        name = index_name,
        dimension = 1536, #default dimension for embedding
        metric = "cosine", #algo used to calculate distance btw vector
        spec = PodSpec(
            environment = "gcp-starter"
        )
    )
    print("index created ")
else:
    print(f"index {index_name} already exists")


#delete index
# if index_name in pc.list_indexes().names():
#     print(f"delete index {index_name}")
#     pc.delete_index(index_name)
#     print("done")
# else:
#     print("index {index_name} does not exists")


#perform actions on index
index = pc.Index(index_name)
print(index.describe_index_stats())
'''
{'dimension': 1536,
 'index_fullness': 0.0, 
 'namespaces': {},
 'total_vector_count': 0}
'''

#inserting random vector
vectors = [[random.random() for _ in range(1536)] for v in range(5)]
print(vectors)
ids = list("abcde")

index_name = "langchain"
index = pc.Index(index_name) #select vector

index.upsert(vectors = zip(ids, vectors)) #link the ids with the vectors

#update vectors
index.upsert(vectors = [("c", [0.5] * 1536)])


#fetch vectors
index = pc.Index(index_name) #select vector
print(index.fetch(ids=["c", "d"]))


#delete vectors
# index.delete(ids=["b", "c"])
# print(index.describe_index_stats())#if we fetch an index that doesnt exists, it will show empty, not an error
# '''{'dimension': 1536,
#  'index_fullness': 3e-05,
#  'namespaces': {'': {'vector_count': 3}},
#  'total_vector_count': 3}
#  '''


print(index.describe_index_stats())


#query 
query_vector = [random.random() for _ in range(1536)]
q = index.query(
    vector=query_vector,
    top_k=3, # return most 3 closest vectors
    include_values = False
)
print(q)



