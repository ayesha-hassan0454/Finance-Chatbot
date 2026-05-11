import streamlit as st
from chatbot import get_response

st.title("💰 Finance Planning Chatbot")

question = st.text_input("Ask your finance question")

if st.button("Ask"):

    if question:

        answer = get_response(question)

        st.success(answer)
