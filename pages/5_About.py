import streamlit as st


st.set_page_config(
    page_title="About Project",
    page_icon="ℹ️",
    layout="wide"
)


st.title("ℹ️ About AI Resume Analyzer")


st.markdown("---")


st.header("📌 Project Overview")


st.write("""
AI Resume Analyzer & Industry Fit Recommendation System is a
Machine Learning based application that analyzes resumes and predicts
the most suitable industry for a candidate.

The system also evaluates resume quality using ATS-style scoring,
identifies skill gaps, and provides personalized career recommendations.
""")


st.markdown("---")


st.header("🎯 Problem Statement")


st.write("""
Many students and job seekers are unsure about:

• Which industry matches their skills

• What skills they are missing

• How strong their resume is

• How to improve their career opportunities

This project solves these problems using Machine Learning and NLP.
""")


st.markdown("---")


st.header("⚙️ Technology Stack")


st.write("""
### Programming Language

🐍 Python


### Data Processing

- Pandas
- NumPy


### Machine Learning

- Scikit-learn

Algorithms Used:

- Logistic Regression
- Decision Tree
- Random Forest
- Naive Bayes
- KNN


### Visualization

- Matplotlib
- Seaborn


### Application

- Streamlit


### Model Saving

- Joblib
""")


st.markdown("---")


st.header("🧠 Machine Learning Workflow")


st.code("""
Resume Dataset

      ↓

Text Cleaning

      ↓

TF-IDF Feature Extraction

      ↓

Machine Learning Models

      ↓

Industry Prediction

      ↓

Resume Scoring Engine

      ↓

Career Recommendations
""")


st.markdown("---")


st.header("✨ Key Features")


features = [

"Resume Upload (PDF/Image/TXT)",

"Industry Prediction",

"Resume Score out of 100",

"ATS Compatibility Score",

"Skill Gap Analysis",

"Strength and Weakness Detection",

"Career Recommendations",

"Multiple ML Model Comparison"

]


for feature in features:

    st.success(feature)


st.markdown("---")


st.header("🚀 Future Enhancements")


st.write("""
Future improvements:

• Deep Learning based resume understanding

• Real-time job recommendation system

• LinkedIn profile analysis

• Resume improvement suggestions

• Interview preparation assistant

• Cloud deployment
""")


st.markdown("---")


st.info(
    "Developed as a Data Science Machine Learning project."
)