from tkinter import *
from PIL import Image, ImageTk  # pip install pillow
from tkinter import ttk, messagebox
import sqlite3


class courseclass:
    def __init__(self, root):
        self.root = root
        self.root.title(" course result")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()

        # title
        title = Label(self.root, text="manage cource ditale", font=(
            "goudy old style", 20, "bold"), bg="#033054", fg="white").place(x=10, y=15, width=1180, height=35)
# =======vriable========
        self.var_course = StringVar()
        self.var_duration = StringVar()
        self.var_charges = StringVar()
        self.var_description = StringVar()

        # ======widget========
        lbl_courseName = Label(self.root, text="course Name", font=(
            "goudy old style", 15, "bold"), bg="white").place(x=10, y=60)
        lbl_duration = Label(self.root, text="duration", font=(
            "goudy old style", 15, "bold"), bg="white").place(x=10, y=100)

        lbl_charges = Label(self.root, text="charges", font=(
            "goudy old style", 15, "bold"), bg="white").place(x=10, y=140)

        lbl_description = Label(self.root, text="description", font=(
            "goudy old style", 15, "bold"), bg="white").place(x=10, y=180)

# =====widget===
        lbl_courseName = Label(self.root, text="course Name", font=(
            "goudy old style", 15, "bold"), bg="white").place(x=10, y=60)
        lbl_duration = Label(self.root, text="duration", font=(
            "goudy old style", 15, "bold"), bg="white").place(x=10, y=100)

        lbl_charges = Label(self.root, text="charges", font=(
            "goudy old style", 15, "bold"), bg="white").place(x=10, y=140)

        lbl_description = Label(self.root, text="description", font=(
            "goudy old style", 15, "bold"), bg="white").place(x=10, y=180)

        # =====entry=====

        self.txt_courseName = Entry(self.root, textvariable=self.var_course, font=(
            "goudy old style", 15, "bold"), bg="lightyellow")
        self.txt_courseName.place(x=150, y=60, width=200)
        txt_duration = Entry(self.root, textvariable=self.var_duration, font=(
            "goudy old style", 15, "bold"), bg="lightyellow").place(x=150, y=100, width=200)

        txt_charges = Entry(self.root, textvariable=self.var_charges, font=(
            "goudy old style", 15, "bold"), bg="lightyellow").place(x=150, y=140, width=200)

        self.txt_description = Text(self.root, font=(
            "goudy old style", 15, "bold"), bg="lightyellow")
        self.txt_description.place(x=150, y=180, width=500, height=140)

        # =====button====
        self.btn_add = Button(self.root, text='save', font=(
            "gound old atyle", 15, "bold"), fg="white", bg="#2196f3", cursor="hand2", command=self.add)
        self.btn_add.place(x=150, y=400, width=110, height=40)
        self.btn_update = Button(self.root, text='update', font=(
            "gound old atyle", 15, "bold"), fg="white", bg="#f39121", cursor="hand2", command=self.update)
        self.btn_update.place(x=270, y=400, width=110, height=40)

        self.btn_delete = Button(self.root, text='delete', font=(
            "gound old atyle", 15, "bold"), fg="white", bg="#a50fdc", cursor="hand2", command=self.delete)
        self.btn_delete.place(x=390, y=400, width=110, height=40)

        self.btn_clear = Button(self.root, text='clear', font=(
            "gound old atyle", 15, "bold"), fg="white", bg="#f32195", cursor="hand2", command=self.clear)
        self.btn_clear.place(x=510, y=400, width=110, height=40)

        # =====search painal========
        self.var_search = StringVar()
        lbl_search_courseName = Label(self.root, text="  course Name", font=(
            "goudy old style", 15, "bold"), bg="white").place(x=720, y=60)
        txt_search_courseName = Entry(self.root, textvariable=self.var_search, font=(
            "goudy old style", 15, "bold"), bg="lightyellow").place(x=850, y=60, width=180)
        btn_search = Button(self.root, text='search', font=(
            "gound old atyle", 15, "bold"), fg="white", bg="#04ec68", cursor="hand2", command=self.search).place(x=1070, y=60, width=120, height=28)

        # =====contants======
        self.C_Frame = Frame(self.root, bd=2, relief=RIDGE)
        self.C_Frame.place(x=720, y=100, width=470, height=340)

        Scrolly = Scrollbar(self.C_Frame, orient=VERTICAL)
        Scrollx = Scrollbar(self.C_Frame, orient=HORIZONTAL)

        self.courseTable = ttk.Treeview(self.C_Frame, columns=(
            "cid", "name", "duration", "charges", "description"), xscrollcommand=Scrollx.set, yscrollcommand=Scrolly.set)
        Scrollx.pack(side=BOTTOM, fill=X)
        Scrolly.pack(side=RIGHT, fill=Y)
        Scrollx.config(command=self.courseTable.xview)
        Scrolly.config(command=self.courseTable.yview)

        self.courseTable.heading("cid", text="course ID")
        self.courseTable.heading("name", text="Name")
        self.courseTable.heading("duration", text="duration")
        self.courseTable.heading("charges", text="charges")
        self.courseTable.heading("description", text="description")

        self.courseTable["show"] = "headings"

        self.courseTable.column("cid", width=50)
        self.courseTable.column("name",  width=100)
        self.courseTable.column("duration",  width=100)
        self.courseTable.column("charges",  width=100)
        self.courseTable.column("description",  width=150)

        self.courseTable.pack(fill=BOTH, expand=1)
        self.courseTable.bind("<ButtonRelease-1>", self.get_data)
        self.show()

# ===================================================================
    def clear(self):
        self.show()
        self.var_course.set("")
        self.var_duration.set("")
        self.var_search.set("")
        self.var_charges.set("")
        self.txt_description.delete('1.0', END)
        self.txt_courseName.config(state="NORMAL")

    def delete(self):

        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_course.get() == "":
                messagebox.showerror(
                    "Error", "course name required", parent=self.root)
            else:
                cur.execute("select * from course where name=?",
                            (self.var_course.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror(
                        "Error", "select course from the list first", parent=self.root)
                else:
                    op = messagebox.askyesno(
                        "confirm", "Do you want to delete", parent=self.root)
                    if op == True:
                        cur.execute("delete from course where name=?",
                                    (self.var_course.get(),))
                        con.commit()
                        messagebox.showinfo(
                            "Delete", "course deleted successfuly", parent=self.root)
                        self.clear()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to{str(ex)}")

    def get_data(self, ev):
        self.txt_courseName.config(state="readonly")
        r = self.courseTable.focus()
        content = self.courseTable.item(r)
        row = content["values"]
        # print(row)
        self.var_course.set(row[1])
        self.var_duration.set(row[2])
        self.var_charges.set(row[3])
        self.txt_description.delete('1.0', END)
        self.txt_description.insert(END, row[4])

    def add(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_course.get() == "":
                messagebox.showerror(
                    "Error", "course name required", parent=self.root)
            else:
                cur.execute("select * from course where name=?",
                            (self.var_course.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror(
                        "Error", "this course is already present, try another", parent=self.root)
                else:
                    cur.execute("insert into course (name, duration, charges, description) values(?,?,?,?)",
                                (self.var_course.get(),
                                 self.var_duration.get(),
                                 self.var_charges.get(),
                                 self.txt_description.get("1.0", END)))

                    con.commit()
                    messagebox.showinfo(
                        "Success", "course added successfully", parent=self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to{str(ex)}")

      # ===========update

    def update(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_course.get() == "":
                messagebox.showerror(
                    "Error", "course name required", parent=self.root)
            else:
                cur.execute("select * from course where name=?",
                            (self.var_course.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror(
                        "Error", "select course from list", parent=self.root)
                else:
                    cur.execute("update course set duration=?, charges=?, description=? where name=?", (

                        self.var_duration.get(),
                        self.var_charges.get(),
                        self.txt_description.get("1.0", END),
                        (self.var_course.get()
                         )))

                    con.commit()
                    messagebox.showinfo(
                        "Success", " course update successfuly", parent=self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to{str(ex)}")

# ============================

    def show(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("select * from course")
            rows = cur.fetchall()
            self.courseTable.delete(*self.courseTable.get_children())
            for row in rows:
                self.courseTable.insert("", END, values=row)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to{str(ex)}")

# =====serch======
    def search(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute(
                f"select * from course where name LIKE '%{self.var_search.get()}%'")
            rows = cur.fetchall()
            self.courseTable.delete(*self.courseTable.get_children())
            for row in rows:
                self.courseTable.insert("", END, values=row)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to{str(ex)}")


if __name__ == "__main__":
    root = Tk()
    obj = courseclass(root)
    root.mainloop()
