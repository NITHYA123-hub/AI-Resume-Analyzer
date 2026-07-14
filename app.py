import streamlit as st

from utils.database import create_table

create_table()

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("📄 AI Resume Analyzer & Industry Fit Recommendation System")

st.markdown("---")

st.write("""
Welcome to the **AI Resume Analyzer**.

This application uses **Machine Learning** to analyze resumes and recommend the most suitable industry based on skills, education, projects, certifications, and experience.

Use the **sidebar** to navigate through the application.
""")

st.info("""
👈 Navigate using the sidebar:

🏠 Home

📄 Upload Resume

📊 Analysis

📈 Model Performance

ℹ️ About
""")

st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Machine Learning Models", "5")

with col2:
    st.metric("Supported Industries", "10")

with col3:
    st.metric("Resume Analysis", "AI Powered")

st.markdown("---")

st.subheader("Project Workflow")

st.code("""
Upload Resume
        ↓
Text Preprocessing
        ↓
TF-IDF Vectorization
        ↓
Random Forest Prediction
        ↓
Resume Score
        ↓
ATS Score
        ↓
Recommendations
""")

st.success("Select 'Upload Resume' from the sidebar to begin.")