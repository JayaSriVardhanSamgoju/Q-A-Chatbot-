from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st 
import os 


from dotenv import load_dotenv

load_dotenv()

#Langsmith tracking 
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_PROJECT"]="Q&AChatbot with Ollama"


prompt=ChatPromptTemplate.from_messages([
    ("system","You are a helpful assistant that answers questions about a given topic."),
    ("user","Question: {question}")
])

def generate_response(question,engine,temperature,max_tokens):
    llm=Ollama(model=engine,temperature=temperature,num_predict=max_tokens)
    output_parser=StrOutputParser()
    chain=prompt | llm | output_parser
    answer=chain.invoke({"question":question})  
    return answer


#Title of the app 
st.title("Enhanced Q&A Chatbot with Ollama")

st.sidebar.title("Settings")
engine=st.sidebar.selectbox("Select Ollama Models ",["phi3:mini","qwen2.5:7b-instruct-q4_K_M"])

temperature=st.sidebar.slider("Temperature",min_value=0.0,max_value=1.0,value=0.7)
max_tokens=st.sidebar.slider("Max Tokens",min_value=1,max_value=300,value=150)

st.write("Go ahead and ask any question ")

user_input=st.text_input("Your Question:")

if user_input:
    response=generate_response(user_input,engine,temperature,max_tokens)
    st.write("Answer:\n",response)
else:
    st.write("Please provide the query ")
    
