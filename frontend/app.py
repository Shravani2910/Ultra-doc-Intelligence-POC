import streamlit as st
import requests

st.title("Ultra Doc Intelligence")

file = st.file_uploader("Upload Document")

if file:
    requests.post("http://localhost:8000/upload", files={"file": file})

query = st.text_input("Ask a question")

if st.button("Ask"):
    res = requests.post("http://localhost:8000/ask", params={"query": query})
    st.write(res.json())

if st.button("Extract Structured Data"):
    res = requests.post("http://localhost:8000/extract")
    st.json(res.json())

try:
    res = requests.post("http://127.0.0.1:8000/upload", files=files)
    st.write(res.status_code)
    st.write(res.text)
except Exception as e:
    st.error(str(e))