# Developer :ul8ziZ
# Date : 6-12 2021

from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from main import *
from Admin_main import *

class login_window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")
        self.root.iconbitmap('Images/icon.ico')

        frame = Frame(self.root, bg="white")
        frame.place(x=610, y=170, width=340, height=450)
        

        img1 = Image.open("images\log.png")
        img1 = img1.resize((100, 100), Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(image=self.photoimage1, bg="white", borderwidth=0)
        lblimg1.place(x=730, y=175, width=100, height=100)

        get_str = Label(frame, text="Get Started", font=("times new roman", 20, "bold"), bg="white", fg="#063970")
        get_str.place(x=100, y=120)

        # labels
        username_lbl = Label(frame, text="Username", font=("times new roman", 15, "bold"), bg="white", fg="#063970")
        username_lbl.place(x=65, y=172)

        self.txtuser = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtuser.place(x=40, y=200, width=270)

        password_lbl = Label(frame, text="Password", font=("times new roman", 15, "bold"), bg="white", fg="#063970")
        password_lbl.place(x=65, y=245)

        self.txtpass = ttk.Entry(frame, show="*",font=("times new roman", 15, "bold"))
        self.txtpass.place(x=40, y=270, width=270)

        # icon.............
        img2 = Image.open("images\icon_user.png")
        img2 = img2.resize((25, 25), Image.ANTIALIAS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        lblimg2 = Label(image=self.photoimage2, bg="white", borderwidth=0)
        lblimg2.place(x=650, y=343, width=25, height=25)

        img3 = Image.open("images\icon_pass.png")
        img3 = img3.resize((25, 25), Image.ANTIALIAS)
        self.photoimage3 = ImageTk.PhotoImage(img3)
        lblimg3 = Label(image=self.photoimage3, bg="white", borderwidth=0,)
        lblimg3.place(x=650, y=415, width=25, height=25)


        # loginBuutton
        loginbtn = Button( command=self.login, text="Login", font=("times new roman", 15, "bold"), bd=3, relief=RIDGE, bg="#063970", fg="white")
        loginbtn.place(x=700, y=500, width=170, height=35)


        #Button_with hover effect
    def on_entera(self):
        loginbtn.config(background= 'darkblue', foreground= '#063970')

    def on_leavea(self):
        loginbtn.config(background='steel blue', foreground= "black")

        loginbtn.bind("<Enter>", on_entera)
        loginbtn.bind("<Leave>", on_leavea)

    def login(self):
        try:    
            if self.txtuser.get() == "" or self.txtpass.get() == "":
                messagebox.showerror("Error", "all field required")
            else:
                conn = mysql.connector.connect(host="localhost", user="root", password="", database="FRAS_DB")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from teacher where Teacher_name=%s and pass=%s",(
                    self.txtuser.get(),
                    self.txtpass.get()

                        ))
                row=my_cursor.fetchone()
                a=row
                if row==None:
                    messagebox.showerror("Error","Invalid username and password")
                else:
                    my_cursor.execute("SELECT type FROM `teacher` WHERE `Teacher_name` = %s AND `pass`=%s",(
                     self.txtuser.get(),
                     self.txtpass.get() ))
                row=my_cursor.fetchone()
                if "Admin" in row:
                    messagebox.showinfo("Welcome  ","Hi "+str(a[1])+"  You are admin")
                    # self.root.destroy()
                    # self.login_window.destroy()
                    self.root.withdraw()
                    self.new_window = Toplevel(self.root)
                    bb = Admin_main(self.new_window) 
                    # self.login_window(self.new_window)

                    # top_level = tk.Toplevel(self)
                    # self.app = Admin_main(top_level, self)
                    # self.app.pack()
                    # self.app.wait_window()

                else:
                    self.root.withdraw()
                    self.new_window = Toplevel(self.root)
                    p = mainn(self.new_window)
                conn.commit()
                conn.close()
        except Exception as es:
                messagebox.showerror("Error", f"You have error here:{str(es)}", parent=self.root)
    
    
if __name__ == "__main__":
    root= Tk()
    app=login_window(root)
    root.mainloop()
