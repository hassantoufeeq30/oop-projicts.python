import sqlite3


def create_db():
    con = sqlite3.connect(database="rms.db")
    cur = con.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS course (cid INTEGER PRIMARY KEY AUTOINCREMENT, Name text, duration TEXT, charges TEXT, description TEXT)")
    con.commit()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS student (roll INTEGER PRIMARY KEY AUTOINCREMENT,Name TEXT, email TEXT, gender TEXT, dob TEXT, contect TEXT, addmission TEXT, course TEXT, state TEXT, city TEXT, pin TEXT, address TEXT)")
    con.commit()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS result (rid INTEGER PRIMARY KEY AUTOINCREMENT,roll TEXT, name text, course TEXT, marks_ob TEXT, full_marks TEXT,per TEXT)")
    con.commit()

    con.close()


def setup_user_table():
    con = sqlite3.connect("rms.db")
    cur = con.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)
    con.commit()
    con.close()


setup_user_table()

create_db()
