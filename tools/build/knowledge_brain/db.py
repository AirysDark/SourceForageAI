import sqlite3
from pathlib import Path

DB_PATH = Path("tools/build/knowledge_brain/brain.db")

def get_db():

    DB_PATH.parent.mkdir(parents=True, exist_ok=True)

    conn = sqlite3.connect(DB_PATH)

    conn.execute("""
    CREATE TABLE IF NOT EXISTS knowledge (

        language TEXT,
        build_file TEXT,
        command TEXT,

        success_count INTEGER DEFAULT 0,
        fail_count INTEGER DEFAULT 0
    )
    """)

    return conn