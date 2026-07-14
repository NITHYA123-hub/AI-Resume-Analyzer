import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import joblib


st.set_page_config(
    page_title="Model Performance",
    page_icon="📈",
    layout="wide"
)


st.title("📈 Machine Learning Model Performance")


st.write("""
This page compares different machine learning algorithms
used for Industry Fit Prediction.
""")


# -------------------------
# Load Model Results
# -------------------------

try:

    results = pd.read_csv(
        "data/model_results.csv"
    )


except:

    st.warning(
        "Model results file not found. Run model training first."
    )

    st.stop()



# -------------------------
# Display Results
# -------------------------

st.header("📊 Model Accuracy Comparison")


st.dataframe(
    results,
    use_container_width=True
)



# -------------------------
# Accuracy Chart
# -------------------------

st.subheader(
    "Accuracy Comparison"
)


fig, ax = plt.subplots()


ax.bar(
    results["Model"],
    results["Accuracy"]
)


ax.set_xlabel(
    "Machine Learning Model"
)


ax.set_ylabel(
    "Accuracy"
)


plt.xticks(
    rotation=45
)


st.pyplot(fig)



# -------------------------
# Best Model
# -------------------------

best_model = results.loc[
    results["Accuracy"].idxmax()
]


st.success(
    f"""
Best Model Selected:

{best_model['Model']}

Accuracy:

{best_model['Accuracy']*100:.2f}%
"""
)



# -------------------------
# Explanation
# -------------------------

st.header("Why Random Forest?")


st.write("""
Random Forest was selected because:

• Handles high-dimensional text features well

• Reduces overfitting compared to single decision trees

• Provides strong classification performance

• Works effectively with TF-IDF features
""")