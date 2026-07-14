from utils.skills import industry_data


def calculate_resume_score(resume_text, predicted_industry):

    resume_text = resume_text.lower()

    details = industry_data[predicted_industry]

    score = 0

    matched_skills = []
    missing_skills = []

    # -------------------------
    # Skills Score (40)
    # -------------------------

    required_skills = details["skills"]

    matched = 0

    for skill in required_skills:

        if skill.lower() in resume_text:

            matched += 1
            matched_skills.append(skill)

        else:

            missing_skills.append(skill)

    skills_score = (matched / len(required_skills)) * 40

    score += skills_score

    # -------------------------
    # Projects Score (20)
    # -------------------------

    project_score = 0

    for project in details["projects"]:

        if project.lower() in resume_text:

            project_score += 10

    project_score = min(project_score, 20)

    score += project_score

    # -------------------------
    # Experience Score (15)
    # -------------------------

    if "2 years" in resume_text:
        score += 15

    elif "1 year" in resume_text:
        score += 12

    elif "internship" in resume_text:
        score += 10

    elif "fresher" in resume_text:
        score += 5

    # -------------------------
    # Certification Score (10)
    # -------------------------

    certification_score = 0

    for cert in details["certifications"]:

        if cert.lower() in resume_text:

            certification_score = 10
            break

    score += certification_score

    # -------------------------
    # Education Score (10)
    # -------------------------

    education_score = 0

    for edu in details["education"]:

        if edu.lower() in resume_text:

            education_score = 10
            break

    score += education_score

    # -------------------------
    # Resume Structure (5)
    # -------------------------

    headings = [
        "education",
        "skills",
        "projects",
        "experience",
        "certification"
    ]

    structure_score = 0

    for heading in headings:

        if heading in resume_text:

            structure_score += 1

    structure_score = structure_score * 1

    score += structure_score

    # -------------------------
    # Final Rating
    # -------------------------

    if score >= 90:
        rating = "Excellent"

    elif score >= 80:
        rating = "Very Good"

    elif score >= 70:
        rating = "Good"

    elif score >= 60:
        rating = "Average"

    else:
        rating = "Needs Improvement"

    return {
        "score": round(score, 2),
        "rating": rating,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills
    }



def analyze_resume(resume_text, predicted_industry):

    result = calculate_resume_score(
        resume_text,
        predicted_industry
    )

    score = result["score"]

    matched = result["matched_skills"]

    missing = result["missing_skills"]

    # ----------------------------
    # ATS Score
    # ----------------------------

    ats_score = score

    headings = [
        "education",
        "skills",
        "projects",
        "experience",
        "certification"
    ]

    heading_count = 0

    text = resume_text.lower()

    for heading in headings:

        if heading in text:

            heading_count += 1

    ats_score += heading_count

    if ats_score > 100:
        ats_score = 100

    # ----------------------------
    # Strengths
    # ----------------------------

    strengths = []

    if "python" in text:
        strengths.append("Strong Python programming skills")

    if "sql" in text:
        strengths.append("Good database knowledge")

    if "machine learning" in text:
        strengths.append("Machine Learning fundamentals")

    if "git" in text:
        strengths.append("Version control knowledge")

    if "streamlit" in text:
        strengths.append("Application deployment skills")

    # ----------------------------
    # Weaknesses
    # ----------------------------

    weaknesses = []

    for skill in missing[:5]:

        weaknesses.append(f"Missing {skill}")

    # ----------------------------
    # Recommendations
    # ----------------------------

    recommendations = []

    recommendation_map = {
        "Statistics": "Learn Statistics and Probability",
        "Docker": "Learn Docker for ML deployment",
        "Power BI": "Learn Power BI for dashboards",
        "Tableau": "Learn Tableau for data visualization",
        "AWS": "Learn AWS Cloud Fundamentals",
        "Azure": "Learn Microsoft Azure",
        "Deep Learning": "Build a Deep Learning project",
        "NLP": "Build an NLP project",
        "Computer Vision": "Build a Computer Vision project",
        "Git": "Practice Git and GitHub workflows"
    }

    for skill in missing:

        if skill in recommendation_map:

            recommendations.append(
                recommendation_map[skill]
            )

    if len(recommendations) == 0:

        recommendations.append(
            "Build more real-world projects."
        )

    return {

        "resume_score": result["score"],

        "rating": result["rating"],

        "ats_score": round(ats_score, 2),

        "matched_skills": matched,

        "missing_skills": missing,

        "strengths": strengths,

        "weaknesses": weaknesses,

        "recommendations": recommendations
    }