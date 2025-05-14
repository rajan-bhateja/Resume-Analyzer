# Resume Analyzer 🧠📄

A Streamlit-powered web app that analyzes resumes and provides valuable **strengths** and **recommendations** using **LangChain** for PDF handling and **Google Gemini** for content analysis.

---

## 🚀 Features

- Upload your resume (PDF format)
- Extract content using `LangChain`'s `PyPDFLoader`
- Send resume content to **Google Gemini 2.0 Flash**
- Get:
  - ✅ 5 good things about your resume
  - 📌 5 personalized improvement suggestions
- Clean UI with **Streamlit**

---

## 🛠️ Tech Stack

- **Python 3.9+**
- [Streamlit](https://streamlit.io/)
- [LangChain](https://www.langchain.com/)
- [Google Generative AI (Gemini)](https://ai.google.dev/)

---

## 📦 Installation

1. **Clone the repository**:

```bash
git clone https://github.com/yourusername/resume-analyzer.git
cd resume-analyzer
```

2. **Install Dependencies**:
```
pip install streamlit langchain google-generativeai
```

3. **Set your Gemini API Key**:
```
genai.configure(api_key="your_gemini_api_key")
```

4. **Run the app**:
```
streamlit run .\analyzer.py
```


