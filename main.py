# Developer :ul8ziZ
# Date : 7-12 2021

from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from Admin_main import *
import os

class mainn:
    def __init__(self, root):
        self.root = root
               
        swidth= root.winfo_screenwidth() 
        sheight= root.winfo_screenheight()
        self.root.geometry("%dx%d" % (swidth, sheight))
        self.root.title("Face Recognition Student Attendance System")
        self.root.iconbitmap('Images/icon.ico')

        # background image
        img4 = Image.open("Images/home.jpg")
        img4 = img4.resize((swidth,sheight), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bg_img = Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=0, width=swidth, height=sheight)

        title_lbl = Label(bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",
                          font=("arial", 35, "bold"), bg="white", fg="black")
        title_lbl.place(x=0, y=0, width=1350, height=45)  
        #  buttons 
        Frame1 = Frame(root, relief=RIDGE, bg="#063970")
        Frame1.place(x=0, y=0, width=swidth, height=210)

        # student button
        img5 = Image.open("Images/student.png")
        img5 = img5.resize((180, 150), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        btn1 = Button(Frame1, image=self.photoimg5, command=self.student_details, cursor="hand2",width=180,height=150  )
        btn1.grid(row=0, column=1,padx=40)

        btn1_1 = Button(Frame1, text="Student Management", command=self.student_details, cursor="hand2", font=("times new roman", 15, "bold"),
        bg="darkblue", fg="white",width="15")
        btn1_1.grid(row=1, column=1,)

        def on_leave(e):
            btn1_1.config(background= 'darkblue', foreground= 'white')
        def on_enter(e):
            btn1_1.config(background='steel blue', foreground= "black")
        
        btn1_1.bind('<Enter>', on_enter)
        btn1_1.bind('<Leave>', on_leave)

        # Face Detection button
        img6 = Image.open("Images/faceDetector.jpg")
        img6 = img6.resize((195, 195), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        btn2 = Button(Frame1, image=self.photoimg6,command=self.face_recognition, cursor="hand2",width=150,height=150)
        btn2.grid(row=0, column=2,padx=10,pady=5)

        btn2_2 = Button(Frame1, text="Tak Attendance",command=self.face_recognition, cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white",width="12")
        btn2_2.grid(row=1, column=2)

        def on_leave(e):
            btn2_2.config(background= 'darkblue', foreground= 'white')
        def on_enter(e):
            btn2_2.config(background='steel blue', foreground= "black")
        
        btn2_2.bind('<Enter>', on_enter)
        btn2_2.bind('<Leave>', on_leave)


        # attendance button
        img7 = Image.open("Images/face.png")
        img7 = img7.resize((150, 150), Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        btn3 = Button(Frame1, image=self.photoimg7,command=self.attendance, cursor="hand2")
        btn3.grid(row=0, column=3,padx=10)

        btn3_3 = Button(Frame1, text="Rabort",command=self.attendance, cursor="hand2", font=("times new roman", 15, "bold"),bg="darkblue", fg="white",width="12")
        btn3_3.grid(row=1, column=3)
        
        def on_leave(e):
            btn3_3.config(background= 'darkblue', foreground= 'white')
        def on_enter(e):
            btn3_3.config(background='steel blue', foreground= "black")
        
        btn3_3.bind('<Enter>', on_enter)
        btn3_3.bind('<Leave>', on_leave)


        # dashboard
        img8 = Image.open("Images/helpdesk.png")
        img8 = img8.resize((150, 150), Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        btn4 = Button(Frame1,image=self.photoimg8,command=self.dashboard, cursor="hand2")
        btn4.grid(row=0, column=4,padx=10)

        btn4_4 = Button(Frame1, text="Dashboard",command=self.dashboard, cursor="hand2", font=("times new roman", 15, "bold"),bg="darkblue", fg="white",width="12")
        btn4_4.grid(row=1, column=4)
        
        def on_leave(e):
            btn4_4.config(background= 'darkblue', foreground= 'white')
        def on_enter(e):
            btn4_4.config(background='steel blue', foreground= "black")
        
        btn4_4.bind('<Enter>', on_enter)
        btn4_4.bind('<Leave>', on_leave)

        # train data button
        img9 = Image.open("Images/trainFace-khom.png")
        img9 = img9.resize((150, 150), Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        btn5 = Button(Frame1, image=self.photoimg9,command=self.train, cursor="hand2")
        btn5.grid(row=0, column=5,padx=10)

        btn5_5 = Button(Frame1, text="Train Data",command=self.train, cursor="hand2", font=("times new roman", 15, "bold"),width="12",
                        bg="darkblue", fg="white")
        btn5_5.grid(row=1, column=5)
        
        def on_leave(e):
            btn5_5.config(background= 'darkblue', foreground= 'white')
        def on_enter(e):
            btn5_5.config(background='steel blue', foreground= "black")
        
        btn5_5.bind('<Enter>', on_enter)
        btn5_5.bind('<Leave>', on_leave)

        # Photos button
        img10 = Image.open("Images/photos.jpg")
        img10 = img10.resize((150, 150), Image.ANTIALIAS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        btn6 = Button(Frame1, image=self.photoimg10, cursor="hand2",command=self.open_img)
        btn6.grid(row=0, column=6,padx=10)

        btn6_6 = Button(Frame1, text="Photos",command=self.open_img, cursor="hand2", font=("times new roman", 15, "bold"),bg="darkblue", fg="white",width="12")
        btn6_6.grid(row=1, column=6)
        
        def on_leave(e):
            btn6_6.config(background= 'darkblue', foreground= 'white')
        def on_enter(e):
            btn6_6.config(background='steel blue', foreground= "black")
        
        btn6_6.bind('<Enter>', on_enter)
        btn6_6.bind('<Leave>', on_leave)

        # About Us
        img11 = Image.open("Images/developer.png")
        img11 = img11.resize((150, 150), Image.ANTIALIAS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        btn7 = Button(Frame1, image=self.photoimg11, cursor="hand2")
        btn7.grid(row=0, column=7,padx=10)

        btn7_7 = Button(Frame1, text="About Us", cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white",width="12")
        btn7_7.grid(row=1, column=7)
        
        def on_leave(e):
            btn7_7.config(background= 'darkblue', foreground= 'white')
        def on_enter(e):
            btn7_7.config(background='steel blue', foreground= "black")
        
        btn7_7.bind('<Enter>', on_enter)
        btn7_7.bind('<Leave>', on_leave)

        # Exit button
        img12 = Image.open("Images/exit-sign-neon-style_77399-144.jpg")
        img12 = img12.resize((150, 150), Image.ANTIALIAS)
        self.photoimg12 = ImageTk.PhotoImage(img12)

        btn8 = Button(Frame1, image=self.photoimg12, cursor="hand2",command=self.exit )
        btn8.grid(row=0, column=8)

        btn8_8 = Button(Frame1, text="Exit",cursor="hand2",command=self.exit,  font=("times new roman", 15, "bold"),  bg="darkblue", fg="white",width="12")    
        btn8_8.grid(row=1, column=8,padx=20)
        
        def on_leave(e):
            btn8_8.config(background= 'darkblue', foreground= 'white')
        def on_enter(e):
            btn8_8.config(background='snow', foreground= "red")
        
        btn8_8.bind('<Enter>', on_enter)
        btn8_8.bind('<Leave>', on_leave)

    # =================================== Functions =========================================

    def student_details(self):
        messagebox.showerror("Error","You are not admin")

    def dashboard(self):
       messagebox.showerror("Error","You are not admin")

    def face_recognition(self):
        self.root.withdraw()
        self.new_window = Toplevel(self.root)
        x = face_recognition(self.new_window) 
        
    def attendance(self):
        messagebox.showerror("Error","You are not admin")

    def train(self):
       messagebox.showerror("Error","You are not admin")

    def open_img(self):
        messagebox.showerror("Error","You are not admin")
    
    def exit(self):
        self.exit=messagebox.askyesno("FRSAS"," Are you sure exit this project ?",parent=self.root)
        if self.exit >0:
           self.root.destroy()
        else:
            return

if __name__ == "__main__":
    root = Tk()
    obj = mainn(root)
    root.mainloop()

