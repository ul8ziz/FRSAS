# Developer :ul8ziZ
# Date : 7-12 2021

from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import os
import numpy as np
import cv2
from mysql.connector import cursor
import mysql.connector
from time import strftime
from datetime import datetime


class face_recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("arial", 30, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=3, width=1530, height=45) 

    #  image
        img1 = Image.open("Images/face-recog-1024x678.jpg")
        img1 = img1.resize((650, 700), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lb2 = Label(self.root, image=self.photoimg1)
        f_lb2.place(x=0, y=55, width=650, height=700)

    #  image 2
        img2 = Image.open("Images/face-recognition-attendance.jpg")
        img2 = img2.resize((950, 700), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=650, y=55, width=950, height=700)

        self.var_depp = StringVar()
        self.var_semester = StringVar()
        self.var_course = StringVar()
        self.var_level = StringVar()

        frame = Frame(self.root, bd=2, bg="white", relief=RIDGE)
        frame.place(x=5, y=120, width=720, height=430)

        # Course
        course_label = Label(frame, text="Course :", font=("Calibri", 10, "bold"), bg="white", fg="blue")
        course_label.grid(row=0, column=2, padx=10, sticky=W)

        conn = mysql.connector.connect(host="localhost",username="root",password="", database="fras_db"    )
        my_cursor = conn.cursor()
        my_cursor.execute("select course_name from courses")
        course_com=my_cursor.fetchall()
        
        course_combo = ttk.Combobox(frame, textvariable=self.var_course, font=("Calibri", 10, "bold"), state="readonly")
        course_combo["values"] = (course_com)
        course_combo.current(0)
        course_combo.grid(row=0, column=3, pady=0, sticky=W)

        # Level
        sem_label = Label(frame, text="Level:", font=("Calibri", 10, "bold"), bg="white", fg="blue")
        sem_label.grid(row=1, column=2, padx=10, sticky=W)

        sem_combo = ttk.Combobox(frame, textvariable=self.var_level, font=("Calibri", 10, "bold"), state="readonly")
        sem_combo["values"] = ("Select Level", "1", "2", "3", "4")
        sem_combo.current(0)
        sem_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        # Semester
        sem_label = Label(frame, text="Semester:", font=("Calibri", 10, "bold"), bg="white", fg="blue")
        sem_label.grid(row=2, column=0, padx=10, sticky=W)

        sem_combo = ttk.Combobox(frame, textvariable=self.var_semester, font=("Calibri", 10, "bold"), state="readonly")
        sem_combo["values"] = ("Select Semester", "1", "2")
        sem_combo.current(0)
        sem_combo.grid(row=2, column=1, padx=2, pady=10, sticky=W)

       #button
        Butt = Button(f_lbl, text="Tak Attendance ",command=self.face_recog, cursor="hand2", font=("times new roman",18, "bold"),bg="darkgreen", fg="white")
        Butt.place(x=365, y=620, width=200, height=40)

    #===============attendance =============================
    def mark_attendance(self,i,n,d):
        with open("Attendance.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i not in name_list)  and (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m:%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"The Atnndans of ,{d}")
                f.writelines(f"\n{i},{n},{d},{dtString},{d1},Preset")
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
                    i="+".join(i)

                    my_cursor.execute("select name from students  where student_id="+str(id))
                    n=my_cursor.fetchone()
                    n="+".join(n)  

                    my_cursor.execute("select dep from students  where student_id="+str(id))
                    d=my_cursor.fetchone()
                    d="+".join(d)    

                    if confidence>77:
                        cv2.putText(img,f"Id:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                        cv2.putText(img,f"Name:{n}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                        cv2.putText(img,f"Department:{d}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
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

if __name__ == "__main__":
    root = Tk()
    obj = face_recognition(root)
    root.mainloop()