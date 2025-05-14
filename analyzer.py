import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
import tempfile

st.set_page_config(layout="wide", page_title="Resume Analyzer")

st.title("Resume Analyzer")
st.caption("Powered by Langchain and Gemini")

try:
    uploaded_resume = st.file_uploader(label="Upload your Resume:", type="pdf")

    if uploaded_resume is not None:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
            tmp_file.write(uploaded_resume.read())
            tmp_file_path = tmp_file.name

        st.subheader("Resume Content:")
        loader = PyPDFLoader(file_path=tmp_file_path, extraction_mode="layout", mode="page")
        docs = loader.load()
        st.write(docs[15].page_content)

except Exception as e:
    st.error(f"An error occurred: {e}")
