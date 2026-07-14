import random
import pandas as pd

from utils.skills import industry_data

first_names = [
    "Rahul",
    "Nithya",
    "Aarav",
    "Priya",
    "Kiran",
    "Rohit",
    "Sneha",
    "Aditya",
    "Pooja",
    "Arjun"
]

last_names = [
    "Sharma",
    "Gowda",
    "Patel",
    "Reddy",
    "Singh",
    "Kumar",
    "Naidu",
    "Shetty",
    "Joshi",
    "Verma"
]

rows = []

for industry, details in industry_data.items():

    for i in range(100):

        name = random.choice(first_names) + " " + random.choice(last_names)

        education = random.choice(details["education"])

        skills = random.sample(details["skills"], 7)

        projects = random.sample(details["projects"], 2)

        experience = random.choice(details["experience"])

        certification = random.choice(details["certifications"])

        summary = (
            f"Motivated {industry} candidate with knowledge of "
            f"{', '.join(skills[:3])}. Passionate about learning "
            f"new technologies and solving real-world problems."
        )

        resume = f"""
Name: {name}

Education:
{education}

Professional Summary:
{summary}

Technical Skills:
{', '.join(skills)}

Projects:
{projects[0]}
{projects[1]}

Experience:
{experience}

Certification:
{certification}
"""

        rows.append({
            "resume": resume,
            "industry": industry
        })

df = pd.DataFrame(rows)

df = df.sample(frac=1, random_state=42).reset_index(drop=True)

df.to_csv("data/resumes.csv", index=False)

print("Dataset Generated Successfully!")
print("Total Rows:", len(df))
print(df.head())