# Developer :ul8ziZ
# Date : 7-12 2021

from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from student import Student
from train import train
from dashboard import dashboard
from face_recognition import face_recognition
from attendance import attendance
import os

class mainn:
    def __init__(self, root):
        self.root = root
               
        swidth= root.winfo_screenwidth() 
        sheight= root.winfo_screenheight()
        self.root.geometry("%dx%d" % (swidth, sheight))
        self.root.title("Face Recognition Student Attendance System")
       
            
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
        Frame1 = Frame(root, relief=RIDGE, bg="RoyalBlue3")
        Frame1.place(x=0, y=0, width=swidth, height=210)

        # student button
        img5 = Image.open("Images/student.jpg")
        img5 = img5.resize((150, 150), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        btn1 = Button(Frame1, image=self.photoimg5, command=self.student_details, cursor="hand2",width=150,height=150 ,borderwidth =0 )
        btn1.grid(row=0, column=1,padx=44)

        btn1_1 = Button(Frame1, text="Student Details", command=self.student_details, cursor="hand2", font=("times new roman", 15, "bold"),
        bg="darkblue", fg="white")
        btn1_1.grid(row=1, column=1)

        def on_leave(e):
            btn1_1.config(background= 'SystemButtonFace', foreground= 'black')
        def on_enter(e):
            btn1_1.config(background='darkblue', foreground= "white")
        
        btn1_1.bind('<Enter>', on_enter)
        btn1_1.bind('<Leave>', on_leave)

        # Face Detection button
        img6 = Image.open("Images/faceDetector.jpeg")
        img6 = img6.resize((195, 195), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        btn2 = Button(Frame1, image=self.photoimg6,command=self.face_recognition, cursor="hand2",width=150,height=150)
        btn2.grid(row=0, column=2,padx=10,pady=5)

        btn2_2 = Button(Frame1, text="Face Detector",command=self.face_recognition, cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        btn2_2.grid(row=1, column=2)

        # attendance button
        img7 = Image.open("Images/face.jpg")
        img7 = img7.resize((150, 150), Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        btn3 = Button(Frame1, image=self.photoimg7,command=self.attendance, cursor="hand2")
        btn3.grid(row=0, column=3,padx=10)

        btn3_3 = Button(Frame1, text="Attendance",command=self.attendance, cursor="hand2", font=("times new roman", 15, "bold"),bg="darkblue", fg="white")
        btn3_3.grid(row=1, column=3)

        # dashboard
        img8 = Image.open("Images/helpdesk.png")
        img8 = img8.resize((150, 150), Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        btn4 = Button(Frame1,image=self.photoimg8,command=self.dashboard, cursor="hand2")
        btn4.grid(row=0, column=4,padx=10)

        btn4_4 = Button(Frame1, text="dashboard",command=self.dashboard, cursor="hand2", font=("times new roman", 15, "bold"),bg="darkblue", fg="white")
        btn4_4.grid(row=1, column=4)

        # train data button
        img9 = Image.open("Images/trainFace-khom.png")
        img9 = img9.resize((150, 150), Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        btn5 = Button(Frame1, image=self.photoimg9,command=self.train, cursor="hand2")
        btn5.grid(row=0, column=5,padx=10)

        btn5_5 = Button(Frame1, text="Train Data",command=self.train, cursor="hand2", font=("times new roman", 15, "bold"),
                        bg="darkblue", fg="white")
        btn5_5.grid(row=1, column=5)

        # Photos button
        img10 = Image.open("Images/photos.jpg")
        img10 = img10.resize((150, 150), Image.ANTIALIAS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        btn6 = Button(Frame1, image=self.photoimg10, cursor="hand2",command=self.open_img)
        btn6.grid(row=0, column=6,padx=10)

        btn6_6 = Button(Frame1, text="Photos",command=self.open_img, cursor="hand2", font=("times new roman", 15, "bold"),bg="darkblue", fg="white")
        btn6_6.grid(row=1, column=6)

        # Developer button
        img11 = Image.open("Images/developer.png")
        img11 = img11.resize((150, 150), Image.ANTIALIAS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        btn7 = Button(Frame1, image=self.photoimg11, cursor="hand2")
        btn7.grid(row=0, column=7,padx=10)

        btn7_7 = Button(Frame1, text="Developer", cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        btn7_7.grid(row=1, column=7)

        # Exit button
        img12 = Image.open("Images/exit-sign-neon-style_77399-144.jpg")
        img12 = img12.resize((150, 150), Image.ANTIALIAS)
        self.photoimg12 = ImageTk.PhotoImage(img12)

        btn8 = Button(Frame1, image=self.photoimg12, cursor="hand2",command=self.exit )
        btn8.grid(row=0, column=8)

        btn8_8 = Button(Frame1, text="Exit",cursor="hand2",command=self.exit,  font=("times new roman", 15, "bold"),  bg="darkblue", fg="white")    
        btn8_8.grid(row=1, column=8,padx=10)

    # =================================== Functions =========================================

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def dashboard(self):
        self.new_window = Toplevel(self.root)
        self.app = dashboard(self.new_window)


    def face_recognition(self):
            self.new_window = Toplevel(self.root)
            self.app = face_recognition(self.new_window)

    def attendance(self):
        self.new_window = Toplevel(self.root)
        self.app = attendance(self.new_window)   

    def train(self):
        self.new_window = Toplevel(self.root)
        self.app = train(self.new_window)   

    def open_img(self):
        os.startfile("data_set")
    
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

