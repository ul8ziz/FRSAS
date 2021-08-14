# Developer :ul8ziZ
# Date : 7-12 2021

from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk  
from tkinter import messagebox
import mysql.connector


class Register:
    def __init__(self, root):
        self.root = root
        self.root.title('Registration Form')
        swidth= root.winfo_screenwidth() 
        sheight= root.winfo_screenheight()
        self.root.geometry("%dx%d" % (swidth, sheight))
        self.root.background="DodgerBlue4"
        # ***************variabletr
        self.var_id = StringVar()
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_type = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()

        # #left image
        self.bg1 = ImageTk.PhotoImage(
            file=r"Images\face-recog-1024x678.jpg")
        left_lbl = Label(self.root, image=self.bg1)
        left_lbl.place(x=50, y=100, width=470, height=550)
        # main frame
        frame = Frame(self.root, bg="white")
        frame.place(x=520, y=100, width=800, height=550)

        register_lbl = Label(frame, text="REGISTER HERE", font=(
            "times new roman", 20, "bold"), fg="#063970", bg="white")
        register_lbl.place(x=20, y=20)

        # ***lebal and entry
        # column 1
        fname = Label(frame, text="First and Middle Name :", font=(
            "times new roman", 15, "bold"), bg="white")
        fname.place(x=50, y=170)

        self.fname_entry = ttk.Entry(
            frame, textvariable=self.var_fname, font=("times new roman", 15))
        self.fname_entry.place(x=50, y=200, width=250)

        # column 2
        contact = Label(frame, text="Contact No :", font=(
            "times new roman", 15, "bold"), bg="white")
        contact.place(x=370, y=170)

        self.txt_contact = ttk.Entry(
            frame, textvariable=self.var_contact, font=("times new roman", 15))
        self.txt_contact.place(x=370, y=200, width=250)

        email = Label(frame, text="Email :", font=(
            "times new roman", 15, "bold"), bg="white")
        email.place(x=370, y=240)

        self.txt_email = ttk.Entry(
            frame, textvariable=self.var_email, font=("times new roman", 15))
        self.txt_email.place(x=370, y=270, width=250)

        # ...........column3
        security_Q = Label(frame, text="Select Type :", font=(
            "times new roman", 15, "bold"), bg="white")
        security_Q.place(x=50, y=240)

        self.combo_security_Q = ttk.Combobox(frame,textvariable=self.var_type, font=(
            "times new roman", 15, "bold"), state="readonly")
        self.combo_security_Q["values"] = (
            "Select", "Admin", "Teacher")
        self.combo_security_Q.place(x=50, y=270, width=250)
        self.combo_security_Q.current(0)

        # ......colum 5
        pswd = Label(frame, text="Password :", font=(
            "times new roman", 15, "bold"), bg="white")
        pswd.place(x=50, y=310)

        self.txt_pswd = ttk.Entry(
            frame, textvariable=self.var_pass, font=("times new roman", 15))
        self.txt_pswd.place(x=50, y=340, width=250)

        confirm_pswd = Label(frame, text="Comform Password :", font=(
            "times new roman", 15, "bold"), bg="white")
        confirm_pswd.place(x=370, y=310)

        self.txt_confirm_pswd = ttk.Entry(
            frame, textvariable=self.var_confpass, font=("times new roman", 15))
        self.txt_confirm_pswd.place(x=370, y=340, width=250)

        # button

        img = Image.open(
            r"Images\7.jpg")
        img = img.resize((200, 50), Image.ANTIALIAS)
        self.photoimage = ImageTk.PhotoImage(img)
        b1 = Button(frame, command=self.register_data,
                    image=self.photoimage, borderwidth=0, cursor="hand2")
        b1.place(x=10, y=420, width=200)

        img1 = Image.open(
            r"Images\8.jpg")
        img1 = img1.resize((200, 50), Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        b1 = Button(frame, image=self.photoimage1,
                    borderwidth=0, cursor="hand2")
        b1.place(x=330, y=420, width=200)

# ................fuction

    def register_data(self):
        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_contact.get() == "" or self.var_pass.get() == "":
            messagebox.showerror("Error", "All fills are required")
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror(
                "Error", "password and confirm password must be same")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="", database="FRAS_DB")
            my_cursor = conn.cursor()
            query = ("select * from Teacher where contact=%s")
            value = (self.var_contact.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row!= None:
                messagebox.showerror("Error", "user already exit ,try another contact noumber")
            else:
                my_cursor.execute("insert into Teacher values(%s,%s,%s,%s,%s,%s)", (
                    self.var_id.get(),
                    self.var_fname.get(),
                    self.var_contact.get(),
                    self.var_email.get(),
                    self.var_type.get(),
                    self.var_pass.get(),
                ))
                messagebox.showinfo("Success","Register Successfully")
            conn.commit()
            conn.close()

if __name__ == "__main__":
    root = Tk()
    app = Register(root)
    root.mainloop()
