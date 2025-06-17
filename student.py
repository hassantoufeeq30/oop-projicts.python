from tkinter import *
from PIL import Image, ImageTk  # pip install pillow
from tkinter import ttk, messagebox
import sqlite3


class studentclass:
    def __init__(self, root):
        self.root = root
        self.root.title(" course result")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()

        # title
        title = Label(self.root, text="manage student details", font=(
            "goudy old style", 20, "bold"), bg="#033054", fg="white").place(x=10, y=15, width=1180, height=35)
# =======vriable========
        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_email = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_contect = StringVar()
        self.var_course = StringVar()
        self.var_a_data = StringVar()
        self.var_state = StringVar()
        self.var_city = StringVar()
        self.var_pin = StringVar()

        # ======widget========
        # ======colume1========
        lbl_roll = Label(self.root, text="Roll No", font=(
            "goudy old style", 15, "bold"), bg="white").place(x=10, y=60)
        lbl_name = Label(self.root, text="Name", font=(
            "goudy old style", 15, "bold"), bg="white").place(x=10, y=100)

        lbl_email = Label(self.root, text="email", font=(
            "goudy old style", 15, "bold"), bg="white").place(x=10, y=140)

        lbl_gender = Label(self.root, text="gender", font=(
            "goudy old style", 15, "bold"), bg="white").place(x=10, y=180)
        lbl_state = Label(self.root, text="state", font=(
            "goudy old style", 15, "bold"), bg="white").place(x=10, y=220)
        txt_state = Entry(self.root, textvariable=self.var_state, font=(
            "goudy old style", 15, "bold"), bg="lightyellow").place(x=150, y=220, width=150)

        lbl_city = Label(self.root, text="city", font=(
            "goudy old style", 15, "bold"), bg="white").place(x=310, y=220)
        txt_city = Entry(self.root, textvariable=self.var_city, font=(
            "goudy old style", 15, "bold"), bg="lightyellow").place(x=380, y=220, width=120)

        lbl_pin = Label(self.root, text="pin", font=(
            "goudy old style", 15, "bold"), bg="white").place(x=510, y=220)
        txt_pin = Entry(self.root, textvariable=self.var_pin, font=(
            "goudy old style", 15, "bold"), bg="lightyellow").place(x=560, y=220, width=120)

        lbl_address = Label(self.root, text="address", font=(
            "goudy old style", 15, "bold"), bg="white").place(x=10, y=260)

        # =====entry=====

        self.txt_roll = Entry(self.root, textvariable=self.var_roll, font=(
            "goudy old style", 15, "bold"), bg="lightyellow")
        self.txt_roll.place(x=150, y=60, width=200)
        txt_name = Entry(self.root, textvariable=self.var_name, font=(
            "goudy old style", 15, "bold"), bg="lightyellow").place(x=150, y=100, width=200)

        txt_email = Entry(self.root, textvariable=self.var_email, font=(
            "goudy old style", 15, "bold"), bg="lightyellow").place(x=150, y=140, width=200)
        self.txt_gender = ttk.Combobox(self.root, textvariable=self.var_gender, values=("select", "male", "female", "other"), font=(
            "goudy old style", 15, "bold"), state="readonly", justify=CENTER)
        self.txt_gender.place(x=150, y=180, width=200)
        self.txt_gender.current(0)

        # ======colume2========
        lbl_dob = Label(self.root, text="D.O.B", font=(
            "goudy old style", 15, "bold"), bg="white").place(x=370, y=60)
        lbl_contect = Label(self.root, text="contect", font=(
            "goudy old style", 15, "bold"), bg="white").place(x=370, y=100)

        lbl_addmission = Label(self.root, text="addmission", font=(
            "goudy old style", 15, "bold"), bg="white").place(x=370, y=140)

        lbl_course = Label(self.root, text="course", font=(
            "goudy old style", 15, "bold"), bg="white").place(x=370, y=180)
        # =====entry2=====
        self.course_list = []

        # =====function calling=====
        self.fetch_course()

        self.dob = Entry(self.root, textvariable=self.var_dob, font=(
            "goudy old style", 15, "bold"), bg="lightyellow").place(x=470, y=60, width=200)
        txt_contect = Entry(self.root, textvariable=self.var_contect, font=(
            "goudy old style", 15, "bold"), bg="lightyellow").place(x=470, y=100, width=200)

        txt_addmission = Entry(self.root, textvariable=self.var_a_data, font=(
            "goudy old style", 15, "bold"), bg="lightyellow").place(x=470, y=140, width=200)
        self.txt_course = ttk.Combobox(self.root, textvariable=self.var_course, values=self.course_list, font=(
            "goudy old style", 15, "bold"), state="readonly", justify=CENTER)
        self.txt_course.place(x=470, y=180, width=200)
        self.txt_course.set("select")


# ========text address========
        self.txt_address = Text(self.root, font=(
            "goudy old style", 15, "bold"), bg="lightyellow")
        self.txt_address.place(x=150, y=260, width=540, height=100)

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
        lbl_search_roll = Label(self.root, text="  roll no", font=(
            "goudy old style", 15, "bold"), bg="white").place(x=720, y=60)
        txt_search_roll = Entry(self.root, textvariable=self.var_search, font=(
            "goudy old style", 15, "bold"), bg="lightyellow").place(x=850, y=60, width=180)
        btn_search = Button(self.root, text='search', font=(
            "gound old atyle", 15, "bold"), fg="white", bg="#04ec68", cursor="hand2", command=self.search).place(x=1070, y=60, width=120, height=28)

        # =====contants======
        self.C_Frame = Frame(self.root, bd=2, relief=RIDGE)
        self.C_Frame.place(x=720, y=100, width=470, height=340)

        Scrolly = Scrollbar(self.C_Frame, orient=VERTICAL)
        Scrollx = Scrollbar(self.C_Frame, orient=HORIZONTAL)

        self.courseTable = ttk.Treeview(self.C_Frame, columns=(
            "roll", "name", "email", "gender", "dob", "contect", "addmission", "course", "state", "city", "pin", "address"), xscrollcommand=Scrollx.set, yscrollcommand=Scrolly.set)
        Scrollx.pack(side=BOTTOM, fill=X)
        Scrolly.pack(side=RIGHT, fill=Y)
        Scrollx.config(command=self.courseTable.xview)
        Scrolly.config(command=self.courseTable.yview)

        self.courseTable.heading("roll", text="roll no")
        self.courseTable.heading("name", text="Name")
        self.courseTable.heading("email", text="email")
        self.courseTable.heading("gender", text="gender")
        self.courseTable.heading("dob", text="D.O.B")
        self.courseTable.heading("contect", text="contect")
        self.courseTable.heading("addmission", text="admission")
        self.courseTable.heading("course", text="coures")
        self.courseTable.heading("state", text="state")
        self.courseTable.heading("city", text="city")
        self.courseTable.heading("pin", text="pin")
        self.courseTable.heading("address", text="address")

        self.courseTable["show"] = "headings"

        self.courseTable.column("roll", width=50)
        self.courseTable.column("name",  width=100)
        self.courseTable.column("email",  width=100)
        self.courseTable.column("gender",  width=100)
        self.courseTable.column("dob",  width=100)
        self.courseTable.column("contect",  width=100)
        self.courseTable.column("addmission",  width=100)
        self.courseTable.column("course",  width=100)
        self.courseTable.column("state",  width=100)
        self.courseTable.column("city",  width=100)
        self.courseTable.column("pin",  width=100)
        self.courseTable.column("address",  width=100)

        self.courseTable.pack(fill=BOTH, expand=1)
        self.courseTable.bind("<ButtonRelease-1>", self.get_data)
        self.show()


# ===================================================================


    def clear(self):
        self.show()
        self.var_roll.set(""),
        self.var_name.set(""),
        self.var_email.set(""),
        self.var_gender.set("select"),
        self.var_dob.set(""),
        self.var_contect.set(""),
        self.var_a_data.set(""),
        self.var_course.set("select"),
        self.var_state.set(""),
        self.var_city.set(""),
        self.var_pin.set(""),
        self.txt_address.delete("1.0", END)
        self.txt_address.insert(END, row[11])
        self.txt_roll.config(state=NORMAL)

    def delete(self):

        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_roll.get() == "":
                messagebox.showerror(
                    "Error", "roll required", parent=self.root)
            else:
                cur.execute("select * from student where roll=?",
                            (self.var_roll.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror(
                        "Error", "select student from the list first", parent=self.root)
                else:
                    op = messagebox.askyesno(
                        "confirm", "Do you want to delete", parent=self.root)
                    if op == True:
                        cur.execute("delete from student where roll=?",
                                    (self.var_roll.get(),))
                        con.commit()
                        messagebox.showinfo(
                            "Delete", "student deleted successfuly", parent=self.root)
                        self.clear()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to{str(ex)}")
# =====get function=========

    def get_data(self, ev):
        self.txt_roll.config(state="readonly")
        r = self.courseTable.focus()
        content = self.courseTable.item(r)
        row = content["values"]
        # print(row)
        self.var_roll.set(row[0]),
        self.var_name.set(row[1]),
        self.var_email.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_dob.set(row[4]),
        self.var_contect.set(row[5]),
        self.var_a_data.set(row[6]),
        self.var_course.set(row[7]),
        self.var_state.set(row[8]),
        self.var_city.set(row[9]),
        self.var_pin.set(row[10]),
        self.txt_address.delete("1.0", END)
        self.txt_address.insert(END, row[11])

    def add(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_roll.get() == "":
                messagebox.showerror(
                    "Error", "roll number required", parent=self.root)
            else:
                cur.execute(
                    "select * from student where roll=?", (self.var_roll.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror(
                        "Error", "roll no is already present, try another", parent=self.root)
                else:
                    cur.execute("insert into student (roll, name, email, gender, dob, contect, addmission, course, state, city, pin, address) values(?,?,?,?,?,?,?,?,?,?,?,?)", (
                                self.var_roll.get(),
                                self.var_name.get(),
                                self.var_email.get(),
                                self.var_gender.get(),
                                self.var_dob.get(),
                                self.var_contect.get(),
                                self.var_a_data.get(),
                                self.var_course.get(),
                                self.var_state.get(),
                                self.var_city.get(),
                                self.var_pin.get(),
                                self.txt_address.get("1.0", END)))

                    con.commit()
                    messagebox.showinfo(
                        "Success", "student added successfully", parent=self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to{str(ex)}")

      # ===========update

    def update(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_roll.get() == "":
                messagebox.showerror(
                    "Error", "roll number required", parent=self.root)
            else:
                cur.execute("select * from student where roll=?",
                            (self.var_roll.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror(
                        "Error", "select student from list", parent=self.root)
                else:
                    cur.execute("update student set name=?, email=?, gender=?, dob=?, contect=?, addmission=?, course=?, state=?, city=?, pin=?, address=? where roll=?", (


                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_contect.get(),
                        self.var_a_data.get(),
                        self.var_course.get(),
                        self.var_state.get(),
                        self.var_city.get(),
                        self.var_pin.get(),
                        self.txt_address.get("1.0", END),
                        self.var_roll.get()))

                    con.commit()
                    messagebox.showinfo(
                        "Success", " student update successfuly", parent=self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to{str(ex)}")

# ============================

    def show(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("select * from student")
            rows = cur.fetchall()
            self.courseTable.delete(*self.courseTable.get_children())
            for row in rows:
                self.courseTable.insert("", END, values=row)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to{str(ex)}")
# ====FACHA======

    def fetch_course(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("select name from course")
            rows = cur.fetchall()

            if len(rows) > 0:
                for row in rows:
                    self.course_list.append(row[0])

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to{str(ex)}")
# =====serch======

    def search(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute(
                f"select * from student where roll=?", (self.var_search.get(),))
            row = cur.fetchone()
            if row != None:

                self.courseTable.delete(*self.courseTable.get_children())
                self.courseTable.insert("", END, values=row)
            else:
                messagebox.showerror(
                    "error", f"no record found", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to{str(ex)}")


if __name__ == "__main__":
    root = Tk()
    obj = studentclass(root)
    root.mainloop()
