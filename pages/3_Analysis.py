import streamlit as st
import matplotlib.pyplot as plt
from utils.ui import load_css
from utils.report import generate_report
from utils.database import save_analysis

from utils.preprocessing import (
    clean_resume,
    extract_name
)

st.set_page_config(
    page_title="Resume Analysis",
    page_icon="📊",
    layout="wide"
)


load_css()


st.title("📊 Resume Analysis Dashboard")


# Check if analysis exists

if "analysis" not in st.session_state:

    st.warning(
        "Please upload and analyze a resume first."
    )

    st.stop()


analysis = st.session_state["analysis"]

industry = st.session_state["industry"]

confidence = st.session_state["confidence"]


# -------------------------
# Prediction Section
# -------------------------

st.header("🎯 Industry Prediction")


col1, col2 = st.columns(2)


with col1:

    st.metric(
        "Recommended Industry",
        industry
    )


with col2:

    st.metric(
        "Prediction Confidence",
        f"{confidence:.2f}%"
    )


st.markdown("---")

candidate_name = extract_name(
    st.session_state["resume_text"]
)


save_analysis(

    candidate_name,

    industry,

    confidence,

    analysis["resume_score"],

    analysis["ats_score"]

)


# -------------------------
# Scores
# -------------------------

st.header("📈 Resume Evaluation")


col1, col2 = st.columns(2)


with col1:

    st.metric(
        "Resume Score",
        f"{analysis['resume_score']}/100"
    )


with col2:

    st.metric(
        "ATS Score",
        f"{analysis['ats_score']}/100"
    )

# -------------------------
# Progress Bars
# -------------------------

st.subheader("📊 Resume Strength")

st.progress(
    int(analysis["resume_score"]) / 100
)

st.write(
    f"{analysis['resume_score']}% Resume Match"
)


st.subheader("🤖 ATS Compatibility")

st.progress(
    int(analysis["ats_score"]) / 100
)

st.write(
    f"{analysis['ats_score']}% ATS Score"
)

# Rating

st.success(
    f"Resume Rating: {analysis['rating']}"
)


st.markdown("---")


# -------------------------
# Skills
# -------------------------

col1, col2 = st.columns(2)


with col1:

    st.subheader(
        "✅ Matched Skills"
    )

    for skill in analysis["matched_skills"]:

        st.success(skill)



with col2:

    st.subheader(
        "❌ Missing Skills"
    )

    for skill in analysis["missing_skills"]:

        st.error(skill)


st.markdown("---")


# -------------------------
# Strengths
# -------------------------

st.header("💪 Strengths")


for item in analysis["strengths"]:

    st.write(
        "✔️",
        item
    )


st.markdown("---")


# -------------------------
# Weaknesses
# -------------------------

st.header("⚠️ Areas to Improve")


for item in analysis["weaknesses"]:

    st.write(
        "🔸",
        item
    )


st.markdown("---")


# -------------------------
# Recommendations
# -------------------------

st.header("🚀 Recommendations")


for item in analysis["recommendations"]:

    st.info(item)


score = analysis["resume_score"]


st.header("📊 Resume Score Visualization")


fig, ax = plt.subplots()


ax.pie(
    [score, 100-score],
    labels=[
        f"Score {score}",
        "Remaining"
    ],
    autopct="%1.1f%%",
    startangle=90
)


ax.axis("equal")


st.pyplot(fig)

# -------------------------
# Download Report
# -------------------------

st.markdown("---")

st.header("📄 Download Report")


report = generate_report(
    industry,
    confidence,
    analysis
)


st.download_button(

    label="⬇️ Download Analysis Report",

    data=report,

    file_name="Resume_Analysis_Report.txt",

    mime="text/plain"

)