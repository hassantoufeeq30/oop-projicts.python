from tkinter import *
from PIL import Image, ImageTk  # pip install pillow
from course import courseclass  # Assuming you have a Course class in course.py
from student import studentclass
from result import resultclass
from report import reportclass
from loin import LoginSystem
from regsiter import RegisterWindow
import sys
import sqlite3


class RMS:
    def __init__(self, root):
        self.root = root
        self.root.title(" student result management system")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")

        # Title

        # title
        title = Label(self.root, text="student result management system", font=(
            "goudy old style", 20, "bold"), bg="#033054", fg="white").place(x=0, y=0, relwidth=1, height=50)


# ====menus====
        M_Frame = LabelFrame(self.root, text="Menu", font=(
            "times new roman", 15, "bold"), bg="white")
        M_Frame.place(x=10, y=50, relwidth=1, height=80, width=1350)

        # buttons
        btn_course = Button(M_Frame, text="Course", font=(
            "goudy old style", 15, "bold"), bg="#2196f3", fg="white",  command=self.add_course).place(x=20, y=5, width=200, height=40)
        btn_student = Button(M_Frame, text="student", font=(
            "goudy old style", 15, "bold"), bg="#2196f3", fg="white", command=self.add_student).place(x=240, y=5, width=200, height=40)
        btn_result = Button(M_Frame, text="result", font=(
            "goudy old style", 15, "bold"), bg="#2196f3", fg="white", command=self.add_result).place(x=460, y=5, width=200, height=40)
        btn_student_result_viwe = Button(M_Frame, text="studentresultviwe", font=(
            "goudy old style", 15, "bold"), bg="#2196f3", fg="white", command=self.add_report).place(x=680, y=5, width=200, height=40)
        btn_logout = Button(M_Frame, text="logout", font=(
            "goudy old style", 15, "bold"), bg="#2196f3", fg="white", command=self.add_login).place(x=900, y=5, width=200, height=40)
        btn_exit = Button(M_Frame, text="exit", font=(
            "goudy old style", 15, "bold"), bg="#2196f3", fg="white", command=self.exit_program).place(x=1120, y=5, width=200, height=40)

       # =======contant======
        """self.bg_img = Image.open("images/bg.jpg")
        self.bg_img = self.bg_img.resize((1350, 550), Image.ANTIALIAS)

        self.bg_img = ImageTk.PhotoImage(self.bg_img)
        self.lbl_bg = Label(self.root, image=self.bg_img).Place(
            x=400, y=180, width=920, height=350)"""
        # =====udate ditale=====
        self.lbl_course = Label(self.root, text="Total Course\n[0]", font=(
            "goudy old style", 20), bg="#F506C5", fg="white", bd=10, relief=RIDGE)
        self.lbl_course.place(x=400, y=530, width=280, height=80)

        self.lbl_STUDENT = Label(self.root, text="Total Course\n[0]", font=(
            "goudy old style", 20), bg="#F506C5", fg="white", bd=10, relief=RIDGE)
        self.lbl_STUDENT.place(x=710, y=530, width=280, height=80)
        self.lbl_result = Label(self.root, text="Total Course\n[0]", font=(
            "goudy old style", 20), bg="#99F506", fg="white", bd=10, relief=RIDGE)
        self.lbl_result.place(x=1020, y=530, width=280, height=80)

        # footer
        footer = Label(self.root, text="student result management system\nfor the contect of tecnical probal", font=(
            "goudy old style", 10, "bold"), bg="#3E06F5", fg="white").pack(side=BOTTOM, fill=X)
        self.update_details()
    # ==============================================

    def update_details(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("select * from course")
            cr = cur.fetchall()
            self.lbl_course.config(text=f"Total Course\n[{str(len(cr))}]")
            self.lbl_course.after(200, self.update_details)

            cur.execute("select * from student")
            cr = cur.fetchall()
            self.lbl_STUDENT.config(text=f"Total student\n[{str(len(cr))}]")
            cur.execute("select * from result")
            cr = cur.fetchall()
            self.lbl_result.config(text=f"Total result\n[{str(len(cr))}]")

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to{str(ex)}")

    def add_course(self):
        self.new_window = Toplevel(self. root)
        self.new_opgj = courseclass(self.new_window)

    def add_student(self):
        self.new_window = Toplevel(self. root)
        self.new_opgj = studentclass(self.new_window)

    def add_result(self):
        self.new_window = Toplevel(self. root)
        self.new_opgj = resultclass(self.new_window)

    def add_report(self):
        self.new_window = Toplevel(self. root)
        self.new_opgj = reportclass(self.new_window)

    def add_login(self):
        self.new_window = Toplevel(self. root)
        self.new_opgj = LoginSystem(self.new_window)

    def exit_program():
        print("\nThank you for using the Student Result Management System.")
        print("Goodbye!\n")
        sys.exit()


if __name__ == "__main__":
    root = Tk()
    obj = RMS(root)
    root.mainloop()
