from pinecone import Pinecone
import os
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer

load_dotenv()
model=SentenceTransformer('all-MiniLM-L6-v2')
pc=Pinecone(api_key=os.getenv('PINECONE_API_KEY'))
index=pc.Index(os.getenv('INDEX_NAME'))

def retriever(query):

    query_trans=model.encode(query).tolist()
    returned_value=index.query(
        vector=query_trans,
        top_k=3,   
        include_metadata=True
    )
    matches = returned_value["matches"]
    context = "\n".join([m["metadata"]["text"] for m in matches])
    return context
