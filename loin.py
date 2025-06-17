from tkinter import *
from tkinter import messagebox
import sqlite3
from regsiter import RegisterWindow


class LoginSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("400x300+500+250")
        self.root.config(bg="white")

        self.username = StringVar()
        self.password = StringVar()

        Label(self.root, text="Login", font=(
            "goudy old style", 20, "bold"), bg="white").pack(pady=10)

        Label(self.root, text="Username", font=(
            "goudy old style", 15), bg="white").place(x=50, y=80)
        Entry(self.root, textvariable=self.username, font=(
            "goudy old style", 15), bg="lightyellow").place(x=160, y=80)

        Label(self.root, text="Password", font=(
            "goudy old style", 15), bg="white").place(x=50, y=130)
        Entry(self.root, textvariable=self.password, font=(
            "goudy old style", 15), bg="lightyellow", show='*').place(x=160, y=130)

        Button(self.root, text="Login", font=("goudy old style", 15),
               bg="#04ec68", command=self.login).place(x=160, y=180)
        Button(self.root, text="Register", font=("goudy old style", 15),
               bg="#0078D7", fg="white", command=self.add_register).place(x=240, y=180)

    def login(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM users WHERE username=? AND password=?",
                        (self.username.get(), self.password.get()))
            row = cur.fetchone()
            if row:
                messagebox.showinfo(
                    "Success", f"Welcome {self.username.get()}!", parent=self.root)
                self.root.destroy()
                # Replace with your main app script name (e.g., result.py)import your_main_app
            else:
                messagebox.showerror(
                    "Error", "Invalid Username or Password", parent=self.root)
        except Exception as ex:
            messagebox.showerror(
                "Error", f"Error: {str(ex)}", parent=self.root)

    def add_register(self):
        self.new_window = Toplevel(self. root)
        self.new_opgj = RegisterWindow(self.new_window)


if __name__ == "__main__":
    root = Tk()
    obj = LoginSystem(root)
    root.mainloop()
