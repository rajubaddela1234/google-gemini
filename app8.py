import streamlit as st
from langchain.llms import ChatClaude  # Import ChatClaude from LangChain
from langchain.agents import Conversations
from langchain.utils import ConversationBufferMemory
import PyPDF2

# Replace with your Claude.ai API key
YOUR_CLAUDE_API_KEY = "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"

# Configure memory for conversation history
memory = ConversationBufferMemory(max_turns=3)

# Create conversation agent with Claude LLM
agent = Conversations(models=[ChatClaude(api_key=YOUR_CLAUDE_API_KEY)], memory=memory)

def load_pdf(uploaded_file):
  """Loads text content from uploaded PDF"""
  pdf_reader = PyPDF2.PdfReader(uploaded_file)
  text = ""
  for page in pdf_reader.pages:
    text += page.extract_text()
  return text

def process_query(query, pdf_text):
  """Sends the query and PDF text to Claude for processing"""
  prompt = f"This document says: {pdf_text}\nBased on the document, answer the following question: {query}"
  response = agent(prompt)
  return response

st.title("PDF Query Chatbot with Claude")

uploaded_file = st.file_uploader("Upload PDF")

if uploaded_file is not None:
  pdf_text = load_pdf(uploaded_file)
  st.write("**PDF Text:**")
  st.write(pdf_text)

  query = st.text_input("Ask a question about the PDF:")

  if query:
    response = process_query(query, pdf_text)
    st.write("**Answer:**")
    st.write(response)
