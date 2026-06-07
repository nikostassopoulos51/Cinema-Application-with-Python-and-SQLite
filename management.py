import sqlite3, hashlib, os

DB_NAME = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cinema.db")

def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def add_movie(title, genre, duration, description, release_date):
    conn = get_connection()
    conn.execute("""
    INSERT INTO movies(title,genre,duration_minutes,description,release_date)
    VALUES(?,?,?,?,?)
    """,(title,genre,duration,description,release_date))
    conn.commit(); conn.close()

def list_movies():
    conn=get_connection()
    data=conn.execute("""
    SELECT id,title,genre,duration_minutes
    FROM movies WHERE is_active=1
    """).fetchall()
    conn.close()
    return data

def delete_movie(movie_id):
    conn=get_connection()
    cur=conn.cursor()
    cur.execute("DELETE FROM movies WHERE id=?", (movie_id,))
    conn.commit()
    deleted = cur.rowcount > 0
    conn.close()
    return deleted

def add_screening(movie_id, location_id, start_time, total_seats):
    conn=get_connection()
    conn.execute("""
    INSERT INTO screenings(movie_id,location_id,start_time,total_seats,available_seats)
    VALUES(?,?,?,?,?)
    """,(movie_id,location_id,start_time,total_seats,total_seats))
    conn.commit(); conn.close()

def list_screenings():
    conn=get_connection()
    data=conn.execute("""
    SELECT s.id,m.title,s.start_time,s.available_seats
    FROM screenings s
    JOIN movies m ON m.id=s.movie_id
    """).fetchall()
    conn.close()
    return data

def delete_screening(screening_id):
    conn=get_connection()
    cur=conn.cursor()
    cur.execute("DELETE FROM screenings WHERE id=?", (screening_id,))
    conn.commit()
    deleted = cur.rowcount > 0
    conn.close()
    return deleted

def add_employee(username,password):
    conn=get_connection()
    conn.execute("""
    INSERT INTO users(username,password_hash,role)
    VALUES (?,?,'employee')
    """,(username,hash_password(password)))
    conn.commit(); conn.close()

def list_employees():
    conn=get_connection()
    data=conn.execute("""
    SELECT id,username FROM users WHERE role='employee'
    """).fetchall()
    conn.close()
    return data

def delete_employee(employee_id):
    conn=get_connection()
    cur=conn.cursor()
    cur.execute("""
    DELETE FROM users
    WHERE id=? AND role='employee'
    """,(employee_id,))
    conn.commit()
    deleted = cur.rowcount > 0
    conn.close()
    return deleted
