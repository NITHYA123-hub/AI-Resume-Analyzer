def find_missing_skills(
    resume_text,
    required_skills
):

    resume_text = resume_text.lower()


    missing = []


    for skill in required_skills.split():

        if skill.lower() not in resume_text:

            missing.append(skill)


    return missing