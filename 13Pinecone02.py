import os
from dotenv import load_dotenv
from pinecone import Pinecone
from pinecone import PodSpec
import random


load_dotenv()

pc = Pinecone()
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

index = pc.Index(index_name)

#namespace => pinecone allow to partition vectors  into namespace. queries and other operation
#are scoped to a specific namespace
#every index consists of one or more namespace.
#each vector exists in exactly one namespace
#unless specified, the namespace will be the "empty" default namespace
    
print(index.describe_index_stats())

'''
Creating index langchain
index created 
{'dimension': 1536,
 'index_fullness': 0.0,
 'namespaces': {},
 'total_vector_count': 0}
 '''

vectors = [[random.random() for _ in range(1536)] for v in range(3)]
ids = list("xyz")
index.upsert(vectors = zip(ids, vectors), namespace ="first-namespace") #link the ids with the vectors

vectors = [[random.random() for _ in range(1536)] for v in range(2)]
ids = list("bo")
index.upsert(vectors = zip(ids, vectors), namespace ="2nd-namespace")

vectors = [[random.random() for _ in range(1536)] for v in range(4)]
ids = list("heri")
index.upsert(vectors = zip(ids, vectors))

print(index.describe_index_stats())
print(index.fetch(ids=['x'])) #going for the "" default namespace => nothing
print(index.fetch(ids=['x'], namespace = "first-namespace")) #find the info on the "first-namespace"
print(index.delete(ids=['x'], namespace = "first-namespace")) #delete the "x" vector => {}
print(index.delete(delete_all=True, namespace ="first-namespace")) #delete everything from the "first-namespace"