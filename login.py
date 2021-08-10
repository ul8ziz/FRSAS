# Developer :ul8ziZ
# Date : 7-12 2021

from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from main import mainn
    


class login_window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        frame = Frame(self.root, bg="black")
        frame.place(x=610, y=170, width=340, height=450)

        img1 = Image.open(
            r"img\2.jpg")

        img1 = img1.resize((100, 100), Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(image=self.photoimage1, bg="black", borderwidth=0)
        lblimg1.place(x=730, y=175, width=100, height=100)

        get_str = Label(frame, text="Get Started", font=(
            "times new roman", 20, "bold"), bg="black", fg="orange")
        get_str.place(x=100, y=100)

        # labels
        username_lbl = Label(frame, text="Username", font=(
            "times new roman", 15, "bold"), bg="black", fg="orange")
        username_lbl.place(x=65, y=152)

        self.txtuser = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtuser.place(x=40, y=180, width=270)

        password_lbl = Label(frame, text="Password", font=(
            "times new roman", 15, "bold"), bg="black", fg="orange")
        password_lbl.place(x=65, y=225)

        self.txtpass = ttk.Entry(frame, show="*",font=("times new roman", 15, "bold"))
        self.txtpass.place(x=40, y=250, width=270)

        # icon.............
        img2 = Image.open(
            r"img\2.jpg")

        img2 = img2.resize((20, 20), Image.ANTIALIAS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        lblimg2 = Label(image=self.photoimage2, bg="black", borderwidth=0)
        lblimg2.place(x=650, y=323, width=25, height=25)

        img3 = Image.open(
            r"img\3.jpg")

        img3 = img3.resize((20, 20), Image.ANTIALIAS)
        self.photoimage3 = ImageTk.PhotoImage(img3)
        lblimg3 = Label(image=self.photoimage3, bg="black", borderwidth=0)
        lblimg3.place(x=650, y=397, width=25, height=25)

        # loginBuutton
        loginbtn = Button(frame, command=self.login, text="Login", font=(
            "times new roman", 15, "bold"), bd=3, relief=RIDGE, bg="red", fg="orange")
        loginbtn.place(x=110, y=300, width=120, height=35)

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
                    messagebox.showinfo("Welcome","Hi "+str(a[1])+"You are admin")
                    self.new_window = Toplevel(self.root)
                    self.app = mainn(self.new_window) 
                    #self.login_window.destroy()
                conn.commit()
                conn.close()
        except Exception as es:
                messagebox.showerror("Error", f"You have error here:{str(es)}", parent=self.root)
    
    
if __name__ == "__main__":
    root= Tk()
    app=login_window(root)
    root.mainloop()
