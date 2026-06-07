from user_access import enter_as_guest, login
from browsing import browse_movies, browse_screenings, book_seats
from management import *

def get_int(prompt):
    try:
        return int(input(prompt))
    except ValueError:
        return None

def guest_menu():
    while True:
        print("\n1. Browse Movies\n2. Exit")
        choice=input("Choice: ")
        if choice=="2":
            return
        if choice!="1":
            continue

        movies=browse_movies()
        for m in movies:
            print(m)

        movie_id=get_int("Movie ID: ")
        if movie_id is None:
            continue

        screenings=browse_screenings(movie_id)
        for s in screenings:
            print(s)

        screening_id=get_int("Screening ID: ")
        if screening_id is None:
            continue

        seats=get_int("Seats: ")
        if seats is None:
            continue

        ok,msg=book_seats(
            screening_id,
            input("Name: "),
            input("Email: "),
            input("Phone: "),
            seats
        )
        print(msg)

def movie_menu():
    print("1.List 2.Add 3.Delete")
    c=input("Choice: ")
    if c=="1":
        for x in list_movies(): print(x)
    elif c=="2":
        add_movie(
            input("Title: "),
            input("Genre: "),
            get_int("Duration: "),
            input("Description: "),
            input("Release date: ")
        )
    elif c=="3":
        print("Deleted" if delete_movie(get_int("Movie ID: ")) else "Not found")

def screening_menu():
    print("1.List 2.Add 3.Delete")
    c=input("Choice: ")
    if c=="1":
        for x in list_screenings(): print(x)
    elif c=="2":
        add_screening(
            get_int("Movie ID: "),
            get_int("Location ID: "),
            input("Start Time: "),
            get_int("Total Seats: ")
        )
    elif c=="3":
        print("Deleted" if delete_screening(get_int("Screening ID: ")) else "Not found")

def employee_menu():
    while True:
        print("\n1.Manage Movies\n2.Manage Screenings\n3.Logout")
        c=input("Choice: ")
        if c=="1": movie_menu()
        elif c=="2": screening_menu()
        elif c=="3": return

def boss_menu():
    while True:
        print("\n1.Manage Movies\n2.Manage Screenings\n3.Manage Employees\n4.Logout")
        c=input("Choice: ")
        if c=="1": movie_menu()
        elif c=="2": screening_menu()
        elif c=="3":
            print("1.List 2.Add 3.Delete")
            s=input("Choice: ")
            if s=="1":
                for e in list_employees(): print(e)
            elif s=="2":
                add_employee(input("Username: "), input("Password: "))
            elif s=="3":
                print("Deleted" if delete_employee(get_int("Employee ID: ")) else "Not found")
        elif c=="4":
            return

def main():
    print("1. Guest\n2. Login")
    c=input("Choice: ")
    if c=="1":
        user=enter_as_guest()
    elif c=="2":
        ok,user=login(input("Username: "), input("Password: "))
        if not ok:
            print("Invalid login")
            return
    else:
        return

    if user["role"]=="guest":
        guest_menu()
    elif user["role"]=="employee":
        employee_menu()
    elif user["role"]=="boss":
        boss_menu()

if __name__ == "__main__":
    main()
