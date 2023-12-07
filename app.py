import os 
import streamlit as st
from langchain.llms import OpenAI
from apikey import apikey
os.environ["OPEN_API_KEY"]=apikey
st.title('Medium Article Generator')
topic = st.text_input('Input your topic of interest')
llm = OpenAI(temperature=1.0)