import pandas as pd
import re


def extract_skills(text):

    text = text.lower()

    skills = [
        "python",
        "sql",
        "pandas",
        "numpy",
        "machine learning",
        "scikit-learn",
        "excel",
        "statistics",
        "powerbi",
        "aws",
        "docker",
        "linux",
        "html",
        "css",
        "javascript",
        "react"
    ]


    matched = []


    for skill in skills:

        if skill.lower() in text:

            matched.append(skill)


    return matched



def recommend_jobs(resume_text):


    jobs = pd.read_csv(
        "data/jobs.csv"
    )


    resume_skills = extract_skills(
        resume_text
    )


    results = []


    for index,row in jobs.iterrows():

        job_skills = row["Skills"].lower()


        matched = 0


        for skill in resume_skills:

            if skill.lower() in job_skills:

                matched += 1


        total = len(
            job_skills.split()
        )


        score = (
            matched / total
        ) * 100


        results.append({

            "Job Title":
            row["Job_Title"],


            "Industry":
            row["Industry"],


            "Match Score":
            round(score,2),


            "Required Skills":
            row["Skills"]

        })


    result_df = pd.DataFrame(results)


    return result_df.sort_values(
        by="Match Score",
        ascending=False
    )