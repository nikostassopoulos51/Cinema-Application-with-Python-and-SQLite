import sqlite3, os

DB_NAME = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cinema.db")

def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

def browse_movies():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
    SELECT id,title,genre,duration_minutes,release_date
    FROM movies
    WHERE is_active=1
    ORDER BY title
    """)
    data = cur.fetchall()
    conn.close()
    return data

def browse_screenings(movie_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
    SELECT s.id,l.name,l.city,s.start_time,s.available_seats,s.total_seats
    FROM screenings s
    JOIN locations l ON l.id=s.location_id
    WHERE s.movie_id=?
    ORDER BY s.start_time
    """,(movie_id,))
    data = cur.fetchall()
    conn.close()
    return data

def book_seats(screening_id,name,email,phone,seat_count):
    conn = get_connection()
    cur = conn.cursor()
    try:
        if seat_count <= 0:
            return False, "Seat count must be greater than 0."

        cur.execute("""
        UPDATE screenings
        SET available_seats = available_seats - ?
        WHERE id=? AND available_seats >= ?
        """,(seat_count,screening_id,seat_count))

        if cur.rowcount == 0:
            conn.rollback()
            return False, "Not enough seats available or screening not found."

        cur.execute("""
        INSERT INTO bookings
        (guest_name,guest_email,guest_phone,screening_id,seat_count)
        VALUES(?,?,?,?,?)
        """,(name,email,phone,screening_id,seat_count))

        conn.commit()
        return True, "Booking successful."
    except Exception as e:
        conn.rollback()
        return False, str(e)
    finally:
        conn.close()
