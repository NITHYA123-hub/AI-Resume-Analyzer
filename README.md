# 🤖 AI Resume Analyzer & Industry Fit Recommendation System

An AI-powered resume intelligence platform that analyzes resumes, predicts suitable industries, evaluates resume quality, identifies skill gaps, and recommends suitable career opportunities using Machine Learning and Natural Language Processing.

---

# 🚀 Features

## 📄 Resume Upload

Supports multiple resume formats:

* PDF
* DOCX
* TXT
* Images (OCR)
* Manual text input

---

## 🧠 AI Industry Prediction

Uses Machine Learning and NLP techniques to predict the best-fit industry based on resume content.

Example:

```
Input:
Resume Skills + Experience

Output:
Recommended Industry:
Data Science

Confidence:
95%
```

---

## 📊 Resume Evaluation

The system calculates:

* Resume Score
* ATS Compatibility Score
* Skill Match Percentage
* Resume Strength Analysis

---

## 🎯 Skill Gap Analysis

Identifies:

✅ Available skills
❌ Missing skills

and suggests areas for improvement.

---

## 💼 AI Job Recommendation

Matches candidate skills with job requirements and recommends suitable roles.

Example:

```
Recommended Jobs:

1. Data Analyst
2. Data Scientist
3. Machine Learning Engineer
```

---

## 📜 Analysis History

Stores previous resume analysis results using SQLite database.

Stores:

* Candidate Name
* Predicted Industry
* Confidence Score
* Resume Score
* ATS Score
* Analysis Date

---

## 📊 Analytics Dashboard

Provides:

* Total candidates analyzed
* Average resume score
* Average ATS score
* Industry distribution charts
* Candidate history overview

---

# 🏗️ Project Architecture

```
AI-Resume-Analyzer/

│
├── app.py
│
├── pages/
│   │
│   ├── 1_Home.py
│   ├── 2_Upload.py
│   ├── 3_Analysis.py
│   ├── 4_Model_Performance.py
│   ├── 5_About.py
│   ├── 6_History.py
│   ├── 7_Job_Recommendation.py
│   └── 8_Analytics.py
│
├── data/
│   │
│   ├── resumes.csv
│   └── jobs.csv
│
├── models/
│   │
│   ├── best_model.pkl
│   └── tfidf.pkl
│
├── utils/
│   │
│   ├── preprocessing.py
│   ├── scoring.py
│   ├── skills.py
│   ├── file_handler.py
│   ├── database.py
│   └── job_recommendation.py
│
├── database/
│   └── history.db
│
├── requirements.txt
│
└── README.md
```

---

# 🛠️ Technology Stack

## Programming Language

* Python

## Machine Learning

* Scikit-learn
* TF-IDF Vectorization
* Classification Algorithms

## NLP

* Text preprocessing
* Resume feature extraction
* Skill extraction

## Data Processing

* Pandas
* NumPy

## Visualization

* Matplotlib
* Streamlit Charts

## Database

* SQLite

## Deployment

* Streamlit Cloud
* GitHub

---

# ⚙️ Installation

Clone repository:

```bash
git clone https://github.com/yourusername/AI-Resume-Analyzer.git
```

Navigate to project:

```bash
cd AI-Resume-Analyzer
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# ▶️ Run Application

Start Streamlit:

```bash
streamlit run app.py
```

---

# 🔄 Workflow

```
Upload Resume

        ↓

Text Extraction

        ↓

NLP Preprocessing

        ↓

TF-IDF Feature Extraction

        ↓

Machine Learning Prediction

        ↓

Resume Scoring

        ↓

Job Recommendation

        ↓

Save Analysis History
```

---

# 📈 Machine Learning Pipeline

```
Resume Dataset

      ↓

Text Cleaning

      ↓

TF-IDF Vectorization

      ↓

Model Training

      ↓

Industry Prediction

      ↓

Performance Evaluation
```

---

# 🎯 Future Enhancements

* Real-time job API integration
* Resume improvement suggestions using Generative AI
* Interview question generation
* Cloud database integration
* User authentication
* Mobile application

---

# 👩‍💻 Author

**Nithya L**

Computer Science Engineering
Data Science Specialization

---

# ⭐ Project Highlights

This project demonstrates practical implementation of:

* Machine Learning
* Natural Language Processing
* Data Analytics
* Streamlit Application Development
* Database Management
* AI-based Career Recommendation

## 🌐 Live Demo

https://ai-resume-analyzer-j89uahnkd3anu6v7rypnta.streamlit.app


## 💻 Source Code

https://github.com/NITHYA123-hub/AI-Resume-Analyzer