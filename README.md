# Cinema-Application-with-Python-and-SQLite

# 🎬 Cinema Booking System

A simple command-line cinema booking system built with **Python** and **SQLite**.

The application supports three user roles:

* **Guest** – browse movies, view screenings, and book seats.
* **Employee** – manage movies and screenings.
* **Boss (Manager)** – manage movies, screenings, and employee accounts.

---

## Features

### Guest

* View available movies
* View movie screenings
* Book cinema seats

### Employee

* Add movies
* List movies
* Delete movies
* Add screenings
* List screenings
* Delete screenings

### Boss

* Full employee permissions
* Create employee accounts
* View employees
* Delete employee accounts

---

## Technologies Used

* Python 3
* SQLite3
* SHA-256 password hashing

---

## Database Structure

### Tables

| Table      | Purpose                       |
| ---------- | ----------------------------- |
| users      | Employee and manager accounts |
| movies     | Movie catalogue               |
| locations  | Cinema locations              |
| screenings | Movie screenings              |
| bookings   | Customer bookings             |

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/cinema-booking-system.git
cd cinema-booking-system
```

2. Initialize the database:

```bash
python init_db.py
```

3. Start the application:

```bash
python main_system.py
```

---

## Default Manager Account

Created automatically when the database is initialized.

```text
Username: boss
Password: admin123
```

Change these credentials before using the system in a real environment.

---

## Project Structure

```text
cinema-booking-system/
│
├── init_db.py
├── main_system.py
├── user_access.py
├── browsing.py
├── management.py
├── cinema.db
└── README.md
```

---

## Example Workflow

### Guest

```text
Browse Movies
    ↓
Select Movie
    ↓
View Screenings
    ↓
Book Seats
```

### Employee

```text
Login
    ↓
Manage Movies
or
Manage Screenings
```

### Boss

```text
Login
    ↓
Manage Movies
Manage Screenings
Manage Employees
```

---

## Future Improvements

* Booking cancellation
* Revenue reports
* Search functionality
* Email validation
* GUI interface (Tkinter/PyQt)
* Web version using Flask or Django

---

## License

This project was created for learning purposes and personal portfolio development.
