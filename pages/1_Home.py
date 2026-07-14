import streamlit as st

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Resume Analyzer & Industry Fit Recommendation System")

st.markdown("---")

st.header("🎯 Project Overview")

st.write("""
This application uses Machine Learning and Natural Language Processing (NLP)
to analyze resumes and recommend the most suitable industry.

The system also evaluates resume quality by calculating a Resume Score,
ATS Score, identifying skill gaps, and providing personalized recommendations.
""")

st.markdown("---")

st.header("🚀 Features")

features = [
    "Predict Best Industry",
    "Resume Score (0-100)",
    "ATS Score",
    "Skill Gap Analysis",
    "Matched Skills",
    "Missing Skills",
    "Strengths & Weaknesses",
    "Career Recommendations",
    "Compare Multiple ML Models"
]

for feature in features:
    st.success(feature)

st.markdown("---")

st.header("🛠 Technology Stack")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Languages & Libraries")
    st.write("""
- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Joblib
- Matplotlib
- Seaborn
""")

with col2:
    st.subheader("Machine Learning Models")
    st.write("""
- Logistic Regression
- Decision Tree
- Random Forest
- Naive Bayes
- KNN
""")

st.markdown("---")

st.header("📌 Workflow")

st.info("""
Resume Upload
      ↓
Text Preprocessing
      ↓
TF-IDF Vectorization
      ↓
Machine Learning Prediction
      ↓
Resume Evaluation
      ↓
Industry Recommendation
""")

st.markdown("---")

st.success("Developed using Python, Scikit-learn and Streamlit.")