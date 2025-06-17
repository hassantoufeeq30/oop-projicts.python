from tkinter import *
from tkinter import messagebox
import sqlite3
# from loin import LoginSystem


class RegisterWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("400x300+500+250")
        self.root.config(bg="white")

        self.username = StringVar()
        self.password = StringVar()
        self.confirm_password = StringVar()

        Label(self.root, text="Register", font=(
            "goudy old style", 20, "bold"), bg="white").pack(pady=10)

        Label(self.root, text="Username", font=(
            "goudy old style", 15), bg="white").place(x=50, y=70)
        Entry(self.root, textvariable=self.username, font=(
            "goudy old style", 15), bg="lightyellow").place(x=160, y=70)

        Label(self.root, text="Password", font=(
            "goudy old style", 15), bg="white").place(x=50, y=120)
        Entry(self.root, textvariable=self.password, font=(
            "goudy old style", 15), bg="lightyellow", show="*").place(x=160, y=120)

        Label(self.root, text="Confirm", font=(
            "goudy old style", 15), bg="white").place(x=50, y=170)
        Entry(self.root, textvariable=self.confirm_password, font=(
            "goudy old style", 15), bg="lightyellow", show="*").place(x=160, y=170)

        Button(self.root, text="Register", font=("goudy old style", 15),
               bg="#04ec68", command=self.register).place(x=160, y=220)
        Button(self.root, text="Back to Login", font=("goudy old style", 12),
               bg="#0078D7", fg="white").place(x=250, y=220)

    def register(self):
        if self.username.get() == "" or self.password.get() == "" or self.confirm_password.get() == "":
            messagebox.showerror(
                "Error", "All fields are required", parent=self.root)
        elif self.password.get() != self.confirm_password.get():
            messagebox.showerror(
                "Error", "Passwords do not match", parent=self.root)
        else:
            try:
                con = sqlite3.connect(database="rms.db")
                cur = con.cursor()
                cur.execute("INSERT INTO users (username, password) VALUES (?,?)",
                            (self.username.get(), self.password.get()))
                con.commit()
                messagebox.showinfo(
                    "Success", "User Registered Successfully", parent=self.root)
                self.root.destroy()
                import login
            except sqlite3.IntegrityError:
                messagebox.showerror(
                    "Error", "Username already exists", parent=self.root)
            except Exception as ex:
                messagebox.showerror(
                    "Error", f"Error: {str(ex)}", parent=self.root)

    # def add_login(self):
       # self.new_window = Toplevel(self. root)
        # self.new_opgj = LoginSystem(self.new_window)


if __name__ == "__main__":
    root = Tk()
    obj = RegisterWindow(root)
    root.mainloop()
