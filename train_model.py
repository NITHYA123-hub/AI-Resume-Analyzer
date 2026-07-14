import pandas as pd
import joblib

from utils.preprocessing import clean_resume

from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.neighbors import KNeighborsClassifier

from sklearn.metrics import accuracy_score


# -------------------------
# Load Dataset
# -------------------------

df = pd.read_csv(
    "data/resumes.csv"
)


print(df.head())


# -------------------------
# Cleaning
# -------------------------

df["clean_resume"] = df["resume"].apply(
    clean_resume
)


X_text = df["clean_resume"]

y = df["industry"]


# -------------------------
# TF-IDF
# -------------------------

tfidf = TfidfVectorizer(
    max_features=3000
)


X = tfidf.fit_transform(
    X_text
)


# -------------------------
# Train Test Split
# -------------------------

X_train, X_test, y_train, y_test = train_test_split(

    X,
    y,
    test_size=0.2,
    random_state=42

)


# -------------------------
# Models
# -------------------------

models = {


    "Logistic Regression":
        LogisticRegression(max_iter=1000),


    "Decision Tree":
        DecisionTreeClassifier(),


    "Random Forest":
        RandomForestClassifier(
            n_estimators=100,
            random_state=42
        ),


    "Naive Bayes":
        MultinomialNB(),


    "KNN":
        KNeighborsClassifier()

}


results = []

best_model = None
best_accuracy = 0
best_name = ""


# -------------------------
# Training
# -------------------------

for name, model in models.items():


    print(
        "Training:",
        name
    )


    model.fit(
        X_train,
        y_train
    )


    prediction = model.predict(
        X_test
    )


    accuracy = accuracy_score(
        y_test,
        prediction
    )


    print(
        name,
        accuracy
    )


    results.append({

        "Model": name,

        "Accuracy": accuracy

    })


    if accuracy > best_accuracy:

        best_accuracy = accuracy

        best_model = model

        best_name = name



# -------------------------
# Save Results
# -------------------------

results_df = pd.DataFrame(
    results
)


results_df.to_csv(
    "data/model_results.csv",
    index=False
)


# -------------------------
# Save Best Model
# -------------------------

joblib.dump(

    best_model,

    "models/best_model.pkl"

)


joblib.dump(

    tfidf,

    "models/tfidf.pkl"

)


print("--------------------")

print(
    "Best Model:",
    best_name
)

print(
    "Accuracy:",
    best_accuracy
)

print(
    "Training Completed!"
)