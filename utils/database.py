import sqlite3
import os
from datetime import datetime


DATABASE_FOLDER = "database"

DATABASE = os.path.join(
    DATABASE_FOLDER,
    "history.db"
)


os.makedirs(
    DATABASE_FOLDER,
    exist_ok=True
)


def create_table():

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS analysis_history(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        name TEXT,

        industry TEXT,

        confidence REAL,

        resume_score INTEGER,

        ats_score INTEGER,

        date TEXT

    )
    """)


    conn.commit()

    conn.close()



def save_analysis(
        name,
        industry,
        confidence,
        resume_score,
        ats_score
):

    # Make sure table exists
    create_table()


    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()


    cursor.execute("""

    INSERT INTO analysis_history
    (
        name,
        industry,
        confidence,
        resume_score,
        ats_score,
        date
    )

    VALUES (?, ?, ?, ?, ?, ?)

    """,
    (
        name,
        industry,
        confidence,
        resume_score,
        ats_score,
        datetime.now().strftime("%d-%m-%Y %H:%M")
    ))


    conn.commit()

    conn.close()

def get_history():

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()


    cursor.execute(
        "SELECT * FROM analysis_history"
    )


    data = cursor.fetchall()


    conn.close()


    return data