import streamlit as st
import joblib

from utils.preprocessing import clean_resume
from utils.scoring import analyze_resume
from utils.file_handler import (
    extract_text_from_pdf,
    extract_text_from_image,
    extract_text_from_txt,
    extract_text_from_docx,
)


# ------------------------
# Load Model
# ------------------------

model = joblib.load("models/best_model.pkl")
vectorizer = joblib.load("models/tfidf.pkl")


st.title("📄 AI Resume Analyzer")

st.write("Upload your resume or paste the text below.")


# ------------------------
# Input Method
# ------------------------

option = st.radio(
    "Choose Resume Input",
    [
        "Upload PDF",
        "Upload Image",
        "Upload TXT",
        "Upload DOCX",
        "Paste Text"
    ]
)


resume_text = ""


# ------------------------
# PDF
# ------------------------

if option == "Upload PDF":

    uploaded_file = st.file_uploader(
        "Upload PDF Resume",
        type=["pdf"]
    )

    if uploaded_file:

        resume_text = extract_text_from_pdf(
            uploaded_file
        )


# ------------------------
# DOCX
# ------------------------

elif option == "Upload DOCX":

    uploaded_file = st.file_uploader(
        "Upload DOCX Resume",
        type=["docx"]
    )

    if uploaded_file:

        resume_text = extract_text_from_docx(
            uploaded_file
        )


# ------------------------
# IMAGE
# ------------------------

elif option == "Upload Image":

    uploaded_file = st.file_uploader(
        "Upload Resume Image",
        type=["png", "jpg", "jpeg"]
    )

    if uploaded_file:

        st.image(
            uploaded_file,
            caption="Uploaded Resume"
        )

        resume_text = extract_text_from_image(
            uploaded_file
        )


# ------------------------
# TXT
# ------------------------

elif option == "Upload TXT":

    uploaded_file = st.file_uploader(
        "Upload TXT Resume",
        type=["txt"]
    )

    if uploaded_file:

        resume_text = extract_text_from_txt(
            uploaded_file
        )


# ------------------------
# PASTE TEXT
# ------------------------

else:

    resume_text = st.text_area(
        "Paste Resume",
        height=350
    )


# ------------------------
# ANALYZE
# ------------------------

if st.button("Analyze Resume"):


    if resume_text.strip() == "":

        st.error(
            "No resume text found."
        )


    else:

        # Save for Job Recommendation
        st.session_state["resume_text"] = resume_text


        cleaned = clean_resume(
            resume_text
        )


        vector = vectorizer.transform(
            [cleaned]
        )


        industry = model.predict(
            vector
        )[0]


        confidence = max(
            model.predict_proba(vector)[0]
        ) * 100


        analysis = analyze_resume(
            resume_text,
            industry
        )


        # Save session data

        st.session_state["analysis"] = analysis

        st.session_state["industry"] = industry

        st.session_state["confidence"] = confidence


        st.success(
            "Resume analyzed successfully!"
        )


        st.subheader(
            "Prediction"
        )


        st.metric(
            "Predicted Industry",
            industry
        )


        st.metric(
            "Confidence",
            f"{confidence:.2f}%"
        )