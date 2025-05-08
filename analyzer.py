import streamlit as st

st.set_page_config(layout="wide", page_title="Resume Analyzer")

st.title("Resume Analyzer")
st.caption("Powered by Langchain and Gemini")

try:
    uploaded_resume = st.file_uploader(label="Upload your Resume:", type="pdf")

    if uploaded_resume.name.endswith(".pdf"):
        st.info("Working on it!")

except:
    st.error("An error occurred!\n \nPlease upload the resume in .pdf format only!")