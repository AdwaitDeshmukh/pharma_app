import sqlite3

DB_NAME = "mydb.sqlite"

def get_db():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT
        );
    """)

    # Insert default user only if table is empty
    cursor.execute("SELECT COUNT(*) as count FROM users")
    if cursor.fetchone()["count"] == 0:
        cursor.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            ("admin", "admin123")  # default username and password
        )

    conn.commit()
    conn.close()
