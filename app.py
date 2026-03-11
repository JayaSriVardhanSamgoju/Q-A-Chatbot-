import streamlit as st 
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
import os 
from dotenv import load_dotenv

load_dotenv()

#Langsmith tracking 
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_PROJECT"]="Q&AChatbot with Groq"

#prompt template 
prompt=ChatPromptTemplate.from_messages([
    ("system","You are a helpful assistant that answers questions about a given topic."),
    ("user","Question: {question}")
])

def generate_response(question,api_key,llm,temperature,max_tokens):
    llm=ChatGroq(model=llm,groq_api_key=api_key,temperature=temperature,max_tokens=max_tokens)
    output_parser=StrOutputParser()
    chain=prompt | llm | output_parser
    answer=chain.invoke({"question":question})  
    return answer


#Title of the app 
st.title("Enhanced Q&A Chatbot with Groq")

st.sidebar.title("Settings")
api_key=st.sidebar.text_input("Enter your Groq API Key",type="password")
llm=st.sidebar.selectbox("LLM",["llama-3.1-8b-instant","llama-3.3-70b-versatile","openai/gpt-oss-120b","openai/gpt-oss-20b"])
temperature=st.sidebar.slider("Temperature",min_value=0.0,max_value=1.0,value=1.0)
max_tokens=st.sidebar.slider("Max Tokens",min_value=1,max_value=8192,value=300)

st.write("Go ahead and ask any question ")

user_input=st.text_input("Your Question:")

if user_input:
    response=generate_response(user_input,api_key,llm,temperature,max_tokens)
    st.write("Answer:\n",response)
else:
    st.write("Please provide the query ")
    