from Raw_generator import RawThesisGeneration
from prompts import role_editor
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from os import getenv
from model_list import model_return
model_name=''
load_dotenv()
token=getenv('HUGGINGFACEHUB_ACCESS_TOKEN')
print(token)
llm=HuggingFaceEndpoint(repo_id=model_return(model_name),
                        task='text-generation',
                        huggingfacehub_api_token=token
                        )

model=ChatHuggingFace(llm=llm)

def editor(query):
    raw_thesis=RawThesisGeneration(query)
    editor_query=f'{role_editor}, here you go is the thesis:: {raw_thesis}'
    final_thesis=model.invoke(editor_query)
    return final_thesis
