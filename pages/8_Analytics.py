import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from utils.database import get_history


st.set_page_config(
    page_title="Analytics",
    page_icon="📊",
    layout="wide"
)


st.title("📊 Candidate Analytics Dashboard")


data = get_history()


if len(data) == 0:

    st.warning(
        "No analysis data available."
    )

    st.stop()



df = pd.DataFrame(
    data,
    columns=[
        "ID",
        "Name",
        "Industry",
        "Confidence",
        "Resume Score",
        "ATS Score",
        "Date"
    ]
)



# ------------------------
# KPI Cards
# ------------------------

col1,col2,col3 = st.columns(3)


with col1:

    st.metric(
        "Total Candidates",
        len(df)
    )


with col2:

    st.metric(
        "Average Resume Score",
        round(
            df["Resume Score"].mean(),
            2
        )
    )


with col3:

    st.metric(
        "Average ATS Score",
        round(
            df["ATS Score"].mean(),
            2
        )
    )


st.divider()


# ------------------------
# Industry Chart
# ------------------------

st.subheader(
    "Industry Distribution"
)


industry_count = (
    df["Industry"]
    .value_counts()
)


fig,ax = plt.subplots()


industry_count.plot(
    kind="bar",
    ax=ax
)


ax.set_xlabel(
    "Industry"
)


ax.set_ylabel(
    "Candidates"
)


st.pyplot(fig)



st.divider()


# ------------------------
# History Table
# ------------------------

st.subheader(
    "Candidate History"
)


st.dataframe(
    df,
    use_container_width=True
)