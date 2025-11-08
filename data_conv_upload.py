from data_input import data
from sentence_transformers import SentenceTransformer
import os
from dotenv import load_dotenv

load_dotenv()
pine_api=os.getenv('PINECONE_API_KEY')

print('data imported')
print('running embeddings algorithm......')

model=SentenceTransformer('all-MiniLM-L6-v2')
embeddings=model.encode(data)

print('data encoded ...... ')

from pinecone import (
    Pinecone,
    ServerlessSpec,
    CloudProvider,
    AwsRegion,
    VectorType
)

pc=Pinecone(api_key=pine_api)

index_name='research-data'
try:
    index_config=pc.create_index(
        name=index_name,
        dimension=384,
        spec=ServerlessSpec(
        cloud=CloudProvider.AWS,
        region=AwsRegion.US_EAST_1),
        vector_type=VectorType.DENSE)
except:
    pass


#idx=pc.Index(host=index_name.host)
idx=pc.Index(index_name)
print('index connected....')
print('upserting records.....')
vectors = []
for i, (text, emb) in enumerate(zip(data, embeddings)):
    vectors.append({
        "id": f"vec{i}",         
        "values": emb,           
        "metadata": {"text": text}  
    })

idx.upsert(vectors)
print("✅ Data upserted successfully!")