from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic

from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from dotenv import load_dotenv
import os
from retriever import retriever
from prompts import role_researcher,role_reviewer,role_editor,role_fc
load_dotenv()

llm = ChatGoogleGenerativeAI(
    model=os.getenv("GEM_MODEL"), 
    google_api_key=os.getenv('GEMINI_API_KEY') )

memory_researcher = ConversationBufferMemory()

conversation_researcher = ConversationChain(
    llm=llm,
    memory=memory_researcher,
    )
role=role_researcher
response=conversation_researcher.predict(input=role)

def researcher(query):
    if query.lower()=='exit' or query.lower()=='quit':
          conversation_researcher.memory.clear()
          conversation_reviewer.memory.clear()
          conversation_fc.memory.clear()
          response=conversation_researcher.predict(input=role)
          return response
    else:
        response_raw=conversation_researcher.predict(input=query)
        if response_raw[0]==0:
             return response_raw[1]
        else:
             retrieved_data=retriever(response_raw[1])
             modified_query=f'here are the relevant data retrieved,again you can analyse and return in the similar formats as specified above in the chat:,{retrieved_data}'
             response_raw=researcher(modified_query)



llm_reviewer=ChatOpenAI(model='gpt-4',temperature=0,api_key=os.getenv('OPENAI_API_KEY'))
memory_reviewer = ConversationBufferMemory()
conversation_reviewer = ConversationChain(
    llm=llm_reviewer,
    memory=memory_reviewer,
    )

response_reviwer=conversation_reviewer.predict(input=role_reviewer)    

def reviewer(thesis):
    response_raw=conversation_reviewer.predict(input=thesis)
    if response_raw[0]==0:
             return response_raw[1]
    else:
        tweeks='here are your tweeks to be done and return the edited thesis in the formats as described'+response_raw[1]
        modified_thesis=researcher(tweeks)
        modified_query=f'here is the modified thesis you go ahead with the same instructions as given  {modified_thesis}'
        response_raw=reviewer(modified_query)

model_fc=ChatAnthropic(model='claude-3-5-sonnet-20241022',api_key=os.getenv('ANTHROPIC_API_KEY'))
memory_fc = ConversationBufferMemory()
conversation_fc = ConversationChain(
    llm=model_fc,
    memory=memory_fc,
    )
response_fc=conversation_reviewer.predict(input=role_fc)    


def fact_checker(thesis):
     raw_response=conversation_fc.predict(input=thesis)
     if raw_response[0]==0:
          return thesis
     else:
        tweeks='here are your factual tweeks to be done and return the edited thesis in the formats as described'+response_raw[1]
        modified_thesis=researcher(tweeks)
        modified_query=f'here is the modified thesis you go ahead with the same instructions as given  {modified_thesis}'
        response_raw=fact_checker(modified_query)

def RawThesisGeneration(query):
     return fact_checker(reviewer(researcher(query)))
          
     
     
     
     
     
     
        

