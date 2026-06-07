import sqlite3, hashlib, os

DB_NAME = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cinema.db")

def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def enter_as_guest():
    return {"id": None, "username": "Guest", "role": "guest"}

def login(username, password):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
    SELECT id, username, role
    FROM users
    WHERE username=? AND password_hash=?
    """, (username, hash_password(password)))
    row = cur.fetchone()
    conn.close()

    if not row:
        return False, None

    return True, {"id": row[0], "username": row[1], "role": row[2]}
