
import sqlite3
import os

DB_PATH = os.path.join("database", "interview.db")

def get_connection():
    os.makedirs("database", exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_connection()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS interviews (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category TEXT NOT NULL,
            difficulty TEXT NOT NULL,
            question TEXT NOT NULL,
            answer TEXT NOT NULL,
            score INTEGER NOT NULL,
            feedback TEXT NOT NULL,
            suggestions TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()

def save_interview(data):
    conn = get_connection()

    conn.execute("""
        INSERT INTO interviews
        (category, difficulty, question, answer,
         score, feedback, suggestions)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        data["category"],
        data["difficulty"],
        data["question"],
        data["answer"],
        data["score"],
        data["feedback"],
        data["suggestions"]
    ))

    conn.commit()
    conn.close()

def get_history():
    conn = get_connection()

    rows = conn.execute("""
        SELECT * FROM interviews
        ORDER BY created_at DESC
    """).fetchall()

    conn.close()
    return [dict(row) for row in rows]
