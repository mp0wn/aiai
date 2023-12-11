import os 
import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from apikey import apikey

# Set the API key in the environment
os.environ["OPENAI_API_KEY"] = apikey

# Streamlit app title
st.title('Medium Article Generator')

# User input for topic and language
topic = st.text_input('Input your topic of interest')
language = st.text_input('Input language')

# Define a template for generating titles
title_template = PromptTemplate(
    input_variables=['topic', 'language'],
    template='Give me a Medium article title on {topic} in {language}'
)

# Create an instance of OpenAI
llm = OpenAI(temperature=0.9)

# Create a chain for processing the prompt
title_chain = LLMChain(llm=llm, prompt=title_template, verbose=True)

# Generate and display the title when a topic is provided
if topic:
    response = title_chain.run({'topic': topic, 'language': language})
    st.write(response)
