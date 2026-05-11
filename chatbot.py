from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

llm = ChatGroq(
    groq_api_key=api_key,
    model_name="llama3-8b-8192"
)

def get_response(question):

    prompt = f"""
    You are a helpful finance assistant.

    Answer this:
    {question}
    """

    response = llm.invoke(prompt)

    return response.content
