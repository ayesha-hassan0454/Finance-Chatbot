import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage

st.set_page_config(page_title="Finance AI Agent", page_icon="💰")

st.title("💰 Finance AI Agent")
st.write("Ask finance-related questions using Groq + LangChain")

# Load API Key
groq_api_key = st.secrets["GROQ_API_KEY"]

# Initialize Model
llm = ChatGroq(
    groq_api_key=groq_api_key,
    model_name="llama3-8b-8192"
)

# User Input
user_input = st.text_input("Enter your finance question:")

if st.button("Ask AI"):
    if user_input:
        with st.spinner("Thinking..."):
            response = llm.invoke([HumanMessage(content=user_input)])
            st.success(response.content)
    else:
        st.warning("Please enter a question.")
