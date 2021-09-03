# Developer :ul8ziZ
# Date : 7-12 2021

from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk  
from tkinter import messagebox
import mysql.connector
from Admin_main import *


class Register:
    def __init__(self, root):
        self.root = root
        self.root.title('Registration Form')
        swidth= root.winfo_screenwidth() 
        sheight= root.winfo_screenheight()
        self.root.geometry("%dx%d" % (swidth, sheight))
        self.root.background="DodgerBlue4"
        self.root.iconbitmap('Images/icon.ico')
        root.state("zoomed")


        # ***************variabletr
        self.var_id = StringVar()
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_type = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()

################# main
        Frame1 = Frame(root, relief=RIDGE, bg="#063970")
        Frame1.place(x=0, y=0, width=swidth, height=110)
        
##########logo
        i = Image.open("Images/icon.png")
        i = i.resize((120, 120))
        self.logo = ImageTk.PhotoImage(i)
        f = Label(Frame1, image=self.logo)
        f.place(x=700, y=-5, width=120, height=120 )

        img6 = Image.open("Images/homee.png")
        img6 = img6.resize((130, 130), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        btn2 = Button(Frame1, image=self.photoimg6, cursor="hand2",width=90,height=90 ,command=self.home)
        btn2.grid(row=0, column=2,padx=10,pady=5)

        # Exit button
        img12 = Image.open("Images/exit-sign-neon-style_77399-144.jpg")
        img12 = img12.resize((90, 90), Image.ANTIALIAS)
        self.photoimg12 = ImageTk.PhotoImage(img12)

        btn88 = Button(Frame1, image=self.photoimg12, cursor="hand2" ,command=self.exite)
        btn88.grid(row=0, column=8,padx=1300)


        # #left image
        self.bg1 = ImageTk.PhotoImage(
            file=r"Images\face-recog-1024x678.jpg")
        left_lbl = Label(self.root, image=self.bg1)
        left_lbl.place(x=110, y=150, width=470, height=550)
        # main frame
        frame = Frame(self.root, bg="white")
        frame.place(x=580, y=150, width=800, height=550)

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
        b1.place(x=40, y=420, width=200)

        

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
    #========= home======================
    def home(self):
        self.root.withdraw()
        self.new_window = Toplevel(self.root)
        bb = Admin_main(self.new_window)  
        
    def exite(self):
             self.exit=messagebox.askyesno("FRSAS"," Are you sure exit this project ?",parent=self.root)
             if self.exit >0:
                  self.root.destroy()
             else:
                  return 

if __name__ == "__main__":
    root = Tk()
    app = Register(root)
    root.mainloop()
