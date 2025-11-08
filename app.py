import streamlit as st
from research_lab import ThesisGenerator
st.title("Welcome to AI Research Lab")



inp=st.chat_input('Enter the topic you want to research on:')
query=str(inp)
st.write(ThesisGenerator(query))
