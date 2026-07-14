from utils.scoring import analyze_resume

resume = """
Education

B.Tech Data Science

Skills

Python
SQL
Pandas
NumPy
Machine Learning
Git
Streamlit

Projects

Customer Churn Prediction

Experience

Internship

Certification

IBM Data Science Professional Certificate
"""

analysis = analyze_resume(
    resume,
    "Data Science"
)

print(analysis)