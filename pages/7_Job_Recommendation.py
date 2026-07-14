import streamlit as st

from utils.job_recommendation import recommend_jobs


st.set_page_config(
    page_title="Job Recommendation",
    page_icon="💼",
    layout="wide"
)


st.title("💼 AI Job Recommendation System")
st.write(st.session_state)


# Check Resume

if "resume_text" not in st.session_state:

    st.warning(
        "Please analyze a resume first."
    )

    st.stop()



resume_text = st.session_state["resume_text"]


industry = st.session_state["industry"]


st.subheader("🎯 Predicted Industry")

st.success(industry)



# Get Recommendations

recommendations = recommend_jobs(
    resume_text
)



st.markdown("---")


st.header("🔥 Recommended Jobs")


top_jobs = recommendations.head(5)



for index,row in top_jobs.iterrows():


    with st.container():


        st.subheader(
            row["Job Title"]
        )


        col1,col2 = st.columns(2)


        with col1:

            st.write(
                "Industry:",
                row["Industry"]
            )


            st.write(
                "Match Score:",
                f"{row['Match Score']}%"
            )


        with col2:

            st.write(
                "Required Skills:"
            )

            st.write(
                row["Required Skills"]
            )


        st.progress(
            int(row["Match Score"])/100
        )


        st.markdown("---")