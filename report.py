from tkinter import *
from PIL import Image, ImageTk  # pip install pillow
from tkinter import ttk, messagebox
import sqlite3


class reportclass:
    def __init__(self, root):
        self.root = root
        self.root.title(" course result")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()

        # Title
        title = Label(self.root, text="View Student Result", font=(
            "goudy old style", 20, "bold"), bg="#04ec68", fg="#262626").pack(side=TOP, fill=X)

        # Variables
        self.var_search = StringVar()
        self.var_roll = StringVar()
        self.var_id = ""

        # Input Roll
        lbl_roll = Label(self.root, text="Enter Roll No.", font=(
            "goudy old style", 15), bg="white").place(x=100, y=100)
        txt_roll = Entry(self.root, textvariable=self.var_search, font=(
            "goudy old style", 15), bg="lightyellow").place(x=250, y=100, width=200)

        btn_search = Button(self.root, text="Search", font=(
            "goudy old style", 15, "bold"), bg="#262626", fg="white", command=self.search).place(x=470, y=98, width=100, height=30)
        self.btn_clear = Button(self.root, text='clear', font=(
            "gound old atyle", 15, "bold"), fg="white", bg="#f32195", cursor="hand2", command=self.clear)
        self.btn_clear.place(x=580, y=98, width=100, height=30)

        """# Result Display Frame
        self.result_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        self.result_frame.place(x=100, y=160, width=500, height=180)

        self.result_label = Label(self.result_frame, text="", font=(
            "goudy old style", 15), bg="white", justify=LEFT)
        self.result_label.pack(pady=20, padx=20)
        """
        # ======ruslt labl =====
        lbl_roll = Label(self.root, text="Roll no", font=(
            "goudy old style", 15, "bold"), bg="white", bd=2, relief=GROOVE).place(x=150, y=230, width=150, height=50)
        lbl_name = Label(self.root, text="Name", font=(
            "goudy old style", 15, "bold"), bg="white", bd=2, relief=GROOVE).place(x=300, y=230, width=150, height=50)

        lbl_course = Label(self.root, text="course", font=(
            "goudy old style", 15, "bold"), bg="white", bd=2, relief=GROOVE).place(x=450, y=230, width=150, height=50)

        lbl_marks = Label(self.root, text="marks", font=(
            "goudy old style", 15, "bold"), bg="white", bd=2, relief=GROOVE).place(x=600, y=230, width=150, height=50)
        lbl_full_marks = Label(self.root, text="total marks", font=(
            "goudy old style", 15, "bold"), bg="white", bd=2, relief=GROOVE).place(x=750, y=230, width=150, height=50)
        lbl_per = Label(self.root, text="persentage", font=(
            "goudy old style", 15, "bold"), bg="white", bd=2, relief=GROOVE).place(x=900, y=230, width=150, height=50)

        self.roll = Label(self.root, font=(
            "goudy old style", 15, "bold"), bg="white", bd=2, relief=GROOVE)
        self.roll.place(x=150, y=280, width=150, height=50)
        self.name = Label(self.root,  font=(
            "goudy old style", 15, "bold"), bg="white", bd=2, relief=GROOVE)
        self.name.place(x=300, y=280, width=150, height=50)

        self.course = Label(self.root, font=(
            "goudy old style", 15, "bold"), bg="white", bd=2, relief=GROOVE)
        self.course.place(x=450, y=280, width=150, height=50)

        self.marks = Label(self.root, font=(
            "goudy old style", 15, "bold"), bg="white", bd=2, relief=GROOVE)
        self.marks.place(x=600, y=280, width=150, height=50)
        self.full = Label(self.root, font=(
            "goudy old style", 15, "bold"), bg="white", bd=2, relief=GROOVE)
        self.full.place(x=750, y=280, width=150, height=50)
        self.per = Label(self.root,  font=(
            "goudy old style", 15, "bold"), bg="white", bd=2, relief=GROOVE)
        self.per.place(x=900, y=280, width=150, height=50)
        # ====button delete======
        self.btn_delete = Button(self.root, text='delete', font=(
            "gound old atyle", 15, "bold"), fg="white", bg="#f32195", cursor="hand2", command=self.delete)
        self.btn_delete.place(x=580, y=400, width=100, height=30)
        # =====================

    def search(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_search.get() == "":
                messagebox.showerror(
                    "Error", "Rollno must be required", parent=self.root)
            else:
                cur.execute(
                    f"select * from result where roll=?", (self.var_search.get(),))
                row = cur.fetchone()
                if row != None:
                    self.var_id = row[0]
                    self.roll.config(text=row[1])
                    self.name.config(text=row[2])
                    self.course.config(text=row[3])
                    self.marks.config(text=row[4])
                    self.full.config(text=row[5])
                    self.per.config(text=row[6])

                else:
                    messagebox.showerror(
                        "error", f"no record found", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to{str(ex)}")

    def clear(self):
        self.var_id = ""
        self.roll.config(text="")
        self.name.config(text="")
        self.course.config(text="")
        self.marks.config(text="")
        self.full.config(text="")
        self.per.config(text="")
        self.var_search.set("")

    def delete(self):

        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_id == "":
                messagebox.showerror(
                    "Error", "search student reuslt first ", parent=self.root)
            else:
                cur.execute("select * from result where rid=?",
                            (self.var_id,))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror(
                        "Error", "enter invalid result", parent=self.root)
                else:
                    op = messagebox.askyesno(
                        "confirm", "Do you want to delete", parent=self.root)
                    if op == True:
                        cur.execute("delete from result where rid=?",
                                    (self.var_id,))
                        con.commit()
                        messagebox.showinfo(
                            "Delete", "result deleted successfuly", parent=self.root)
                        self.clear()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to{str(ex)}")


if __name__ == "__main__":
    root = Tk()
    obj = reportclass(root)
    root.mainloop()
