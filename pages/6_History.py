import streamlit as st
import pandas as pd

from utils.database import get_history


st.title("📜 Resume Analysis History")


data = get_history()


if len(data) == 0:

    st.info(
        "No analysis history available."
    )

else:

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


    st.dataframe(
        df,
        use_container_width=True
    )