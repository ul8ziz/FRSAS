# Developer :ul8ziZ
# Date : 7-12 2021

from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import os
import numpy as np
import urllib.request
import urllib.request

import cv2
import mysql.connector
from mysql.connector import cursor
from time import strftime
from datetime import datetime
from Admin_main import *


class face_recognition:
    def __init__(self, root):
        self.root = root
        swidth= root.winfo_screenwidth()
        sheight= root.winfo_screenheight()
        self.root.geometry("%dx%d" % (swidth, sheight))
        # self.root.geometry(1000*1000)
        root.state("zoomed")
        self.root.title("Attendance System")
        self.root.iconbitmap("images/icon.ico")
        
        self.level = StringVar()
        self.semester = StringVar()
        self.course = StringVar()
        self.camer = StringVar()

        def donothing():
            filewin = Toplevel(self.root)
            button = Button(filewin, text="Do nothing button")
            button.pack()
            
        menubar = Menu(self.root)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", command=donothing)
        filemenu.add_command(label="Open", command=donothing)
        filemenu.add_command(label="Save", command=donothing)
        filemenu.add_command(label="Save as...", command=donothing)
        filemenu.add_command(label="Close", command=donothing)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.root.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        editmenu = Menu(menubar, tearoff=0)
        editmenu.add_command(label="Undo", command=donothing)
        editmenu.add_separator()
        editmenu.add_command(label="Cut", command=donothing)
        editmenu.add_command(label="Copy", command=donothing)
        editmenu.add_command(label="Paste", command=donothing)
        editmenu.add_command(label="Delete", command=donothing)
        editmenu.add_command(label="Select All", command=donothing)
        menubar.add_cascade(label="Edit", menu=editmenu)
        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Help Index", command=donothing)
        helpmenu.add_command(label="About...", command=donothing)
        menubar.add_cascade(label="Help", menu=helpmenu)
        self.root.config(menu=menubar)

        statusbar = Label(root, text="on the way…", bd=1, relief=SUNKEN, anchor=W)
        statusbar.pack(side=BOTTOM, fill=X)

    #  image
        img1 = Image.open("Images/face-recog-1024x678.jpg")
        img1 = img1.resize((650, 662), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lb2 = Label(self.root, image=self.photoimg1)
        f_lb2.place(x=0, y=100, width=650, height=662)

    #  image 2
        img2 = Image.open("Images/face-recognition-attendance.jpg")
        img2 = img2.resize((950, 700), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img2)
        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=650, y=100, width=950, height=662)

        
##########logo

        Frame1 = Frame(root, relief=RIDGE, bg="#063970")
        Frame1.place(x=0, y=0, width=swidth, height=110)
       
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
        
        frame = Frame(self.root, bd=2, bg="#063970", relief=RIDGE)
        frame.place(x=100, y=400, width=800, height=100)

        # Department
        dep_label = Label(frame, text="Department :", font=("Calibri", 10, "bold"), bg="#063970",fg="white")
        dep_label.grid(row=0, column=1, padx=0, sticky=W)

        conn = mysql.connector.connect(host="localhost",username="root",password="", database="fras_db"    )
        my_cursor = conn.cursor()
        my_cursor.execute("select Department_name from department")
        depcom=my_cursor.fetchall()
        
        dep_combo = ttk.Combobox(frame, font=("Calibri", 10, "bold"), width=11, state="readonly")
        dep_combo["values"] = (depcom)
        dep_combo.current(0)
        dep_combo.grid(row=0, column=2, padx=10,pady=0, sticky=W)

        # Level
        sem_label = Label(frame, text="Level:", font=("Calibri", 10, "bold"), bg="#063970", fg="white")
        sem_label.grid(row=0, column=3, padx=0, sticky=W)

        sem_combo = ttk.Combobox(frame, textvariable=self.level, font=("Calibri", 10, "bold"),width=11, state="readonly")
        sem_combo["values"] = ("Select ", "1", "2", "3", "4")
        sem_combo.current(0)
        sem_combo.grid(row=0, column=4, padx=10, pady=0, sticky=W)

        # Semester
        sem_label = Label(frame, text="Semester:", font=("Calibri", 10, "bold"), bg="#063970", fg="white")
        sem_label.grid(row=0, column=5, padx=0, sticky=W)

        sem_combo = ttk.Combobox(frame, textvariable=self.semester, font=("Calibri", 10, "bold"),width=11, state="readonly")
        sem_combo["values"] = ("Select", "1", "2")
        sem_combo.current(0)
        sem_combo.grid(row=0, column=6, padx=10, pady=10, sticky=W)

        # Course
        course_label = Label(frame, text="Course :", font=("Calibri", 10, "bold"), bg="#063970", fg="white")
        course_label.grid(row=1, column=1, padx=0, sticky=W)

        conn = mysql.connector.connect(host="localhost",username="root",password="", database="fras_db"    )
        my_cursor = conn.cursor()
        my_cursor.execute("select course_name from courses")
        course_com=my_cursor.fetchall()
        
        course_combo = ttk.Combobox(frame, textvariable=self.course, font=("Calibri", 10, "bold"),width=11, state="readonly")
        course_combo["values"] = (course_com)
        course_combo.current(0)
        course_combo.grid(row=1, column=2, padx=10, sticky=W)
        # number of lecturer
        course_label = Label(frame, text="Number of lecturer :", font=("Calibri", 10, "bold"), bg="#063970", fg="white")
        course_label.grid(row=1, column=3, padx=0, sticky=W)
        
        course_combo = ttk.Combobox(frame, font=("Calibri", 10, "bold"),width=11,)
        course_combo["values"] = ("Select","1", "2","3", "4","5", "6","7", "8","9", "10","11", "12")
        course_combo.current(0)
        course_combo.grid(row=1, column=4, padx=20, sticky=W)
        # Teacher
        course_label = Label(frame, text="Teacher Name :", font=("Calibri", 10, "bold"), bg="#063970", fg="white")
        course_label.grid(row=1, column=5, padx=0, sticky=W)
        conn = mysql.connector.connect(host="localhost",username="root",password="", database="fras_db"    )
        my_cursor = conn.cursor()
        my_cursor.execute("select Teacher_name from Teacher")
        teacher=my_cursor.fetchall()
        
        course_combo = ttk.Combobox(frame, font=("Calibri", 10, "bold"),width=11,)
        course_combo["values"] = (teacher)
        course_combo.current(0)
        course_combo.grid(row=1, column=6, padx=0, sticky=W)

        #button
        Butt = Button(f_lbl, text=" Start Tak Attendance ",command=self.face_recog, cursor="hand2", font=("times new roman",18, "bold"),bg="white", fg="black")
        Butt.place(x=390, y=300, width=300, height=40)

        #Camre number
        Camre = Label(f_lbl, text="Camre number:", font=("times new roman", 14, "bold"), bg="white", fg="black")
        Camre.place(x=390, y=350, width=195, height=30)

        Camre = ttk.Combobox(f_lbl, textvariable=self.camer, font=("Calibri", 14, "bold"),width=11, state="readonly")
        Camre["values"] = ( "0","1",)
        Camre.current(0)
        Camre.place(x=590, y=350, width=100, height=30)

        #report
        Butt1 = Button(f_lbl, text="Go to Report  ",command=self.report, cursor="hand2", font=("times new roman",18, "bold"),bg="white", fg="black")
        Butt1.place(x=390, y=580, width=200, height=40)
        
    #===============attendance =============================
    def mark_attendance(self,i,n,d):
        try:  
                conn = mysql.connector.connect(host="localhost",username="root",password="",database="FRAS_DB")                                              
                my_cursor = conn.cursor()
                now=datetime.now()
                d1=now.strftime("%d/%m/:%Y")
                dtString=now.strftime("%H:%M:%S")
                self.attendance_id =i
                self.student_name = n
                self.dep = d
                self.Time = dtString
                self.Date = d1
                self.State="Preset"
                
                my_cursor.execute("INSERT INTO `attendance` ( `attendance_id`,`student_name`, `dep`, `Time`, `Date`, `level`, `semester`, `course`, `State`)values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                        (
                            self.attendance_id,
                            self.student_name,
                            self.dep,
                            self.Time,
                            self.Date,
                            self.level.get(),
                            self.semester.get(),
                            self.course.get(),
                            self.State
                        ))
                conn.commit()
                conn.close()
        except Exception as es:
                messagebox.showerror("Error", f"because of :{str(es)}", parent=self.root)
    #===================Face Recongnition ============
    def face_recog(self):
        try:
            
            def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
                gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)
                coord=[]
                for(x,y,w,h) in features:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                    id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                    confidence=int((100*(1-predict/300)))

                    conn = mysql.connector.connect(host="localhost",username="root",password="",database="fras_db")                                              
                    my_cursor = conn.cursor()
                    my_cursor.execute("select student_id from students  where student_id="+str(id))
                    i=my_cursor.fetchone()
                    # i=str(i)
                    i="+".join(i)

                    my_cursor.execute("select Name from students  where student_id="+str(id))
                    n=my_cursor.fetchone()
                    # n=str(n)  
                    n="+".join(n)

                    my_cursor.execute("select Dep from students  where student_id="+str(id))
                    d=my_cursor.fetchone()
                    d="+".join(d)

                    if confidence>77:
                        cv2.putText(img,f"Id :{i}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                        cv2.putText(img,f"Name :{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                        cv2.putText(img,f"Department :{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                        self.mark_attendance(i,n,d)
                    else:
                        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                        cv2.putText(img,f"UnKnown Fcace",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                    coord=[x,y,w,h]
                return coord
                                        
            def recongnize(img,clf,faceCascade):
                coord=draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
                return img
            faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
            clf=cv2.face.LBPHFaceRecognizer_create() 
            clf.read("classifier.xml")
           # ipcam="http://192.168.1.2:4747/video"
            cam_num=self.camer.get()
            video_cap=cv2.VideoCapture(0)
            while True:
                ret,img=video_cap.read()
                img=recongnize(img,clf,faceCascade)
                cv2.imshow("Welcome To Face Recognition",img)
                if cv2.waitKey(10) & 0xFF == ord('q'): 
                    break
            video_cap.release()
            cv2.destroyAllWindows()
        except Exception as es:
                messagebox.showerror("Error", f"because of :{str(es)}", parent=self.root)   
     #========= home======================
    def home(self):
        self.root.withdraw()
        self.new_window = Toplevel(self.root)
        s = Admin_main(self.new_window)
        
    def exite(self):
             self.exit=messagebox.askyesno("FRSAS"," Are you sure exit this project ?",parent=self.root)
             if self.exit >0:
                  self.root.destroy()
             else:
                  return 

    def report(self):
            self.root.withdraw()
            self.new_window = Toplevel(self.root)
            d = attendance(self.new_window)

if __name__ == "__main__":
    root = Tk()
    obj = face_recognition(root)
    root.mainloop()