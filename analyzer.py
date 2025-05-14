import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
import tempfile
import google.generativeai as genai

st.set_page_config(layout="wide", page_title="Resume Analyzer")

st.title("Resume Analyzer")
st.caption("Powered by Langchain and Gemini")

try:
    uploaded_resume = st.file_uploader(label="Upload your Resume:", type="pdf")

    if uploaded_resume is not None:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
            tmp_file.write(uploaded_resume.read())
            tmp_file_path = tmp_file.name

        st.subheader("Recommendations and Suggestions:")
        loader = PyPDFLoader(file_path=tmp_file_path, extraction_mode="layout", mode="single")
        docs = loader.load()
        # st.write(docs[0].page_content)

        genai.configure(api_key="gemini_api_key")

        client = genai.GenerativeModel("gemini-2.0-flash")
        response = client.generate_content(
            contents=f"Mention 5 good things and suggest 5 recommendations for the resume {docs[0].page_content}"
        )

        st.markdown(response.text)

except Exception as e:
    st.error(f"An error occurred: {e}")
