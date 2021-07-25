# Developer : Ul8ziZ
# Date : Saturday, 7-12- 2021

from os import error
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from mysql.connector import cursor
import cv2


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1600x900+0+0")
        self.root.title("FRAS")
        # ==================================variables ========================================
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div=StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob= StringVar()
        self.var_email= StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher= StringVar()

        # first image
        img1 = Image.open("Images/smart-attendance.jpg")
        img1 = img1.resize((1600, 100), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=0, y=0, width=1600, height=120)

        # background image
        img4 = Image.open("Images/face-recognition-logo.jpeg")
        img4 = img4.resize((1600, 1000), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bg_img = Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=120, width=1600, height=1000)

        title_lbl = Label(bg_img, text="STUDENT MANAGEMENT SYSTEM",font=("times new roman", 20, "bold"), bg="white", fg="black")
        title_lbl.place(x=0, y=0, width=1600, height=50) 

        main_frame = Frame(bg_img, bd=2)
        main_frame.place(x=10, y=80, width=1500, height=1000)

         # left label frame
        Left_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Information", font=("Calibri", 12, "bold"))
        Left_frame.place(x=0, y=0, width=730, height=600)

        img_left = Image.open("Images/grad2.jpg")
        img_left = img_left.resize((720, 130), Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=720, height=130)
       
         # Right label frame
        Right_frame = LabelFrame(main_frame, bd=2,bg="white",relief=RIDGE, text="Student Details", font=("Calibri", 12, "bold"))
        Right_frame.place(x=750, y=10, width=740, height=600)

        img_right = Image.open("Images/grad2.jpg")
        img_right = img_right.resize((720, 120), Image.ANTIALIAS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(Right_frame, image=self.photoimg_right)
        f_lbl.place(x=5, y=0, width=710, height=120)

        #============current course frame================
        current_course_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Current Course Information",font=("Calibri", 13, "bold"), fg="green")
        current_course_frame.place(x=5, y=135, width=720, height=200)
        
        # Department
        dep_label = Label(current_course_frame, text="Department :", font=("Calibri", 10, "bold"), bg="white", fg="blue")
        dep_label.grid(row=0, column=0, padx=10, sticky=W)

        dep_combo = ttk.Combobox(current_course_frame, textvariable=self.var_dep, font=("Calibri", 10, "bold"), state="readonly")
        dep_combo["values"] = ("Select Department", "cs", "IT", "Electronics", "Civil")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, pady=10, sticky=W)

        # Course
        course_label = Label(current_course_frame, text="Course :", font=("Calibri", 10, "bold"), bg="white", fg="blue")
        course_label.grid(row=0, column=2, padx=10, sticky=W)

        course_combo = ttk.Combobox(current_course_frame, textvariable=self.var_course, font=("Calibri", 10, "bold"), state="readonly")
        course_combo["values"] = ("Select Course", "C++", "Jave", "php", "web", "A+")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, pady=0, sticky=W)

        # Year
        year_label = Label(current_course_frame, text="Year :", font=("Calibri", 10, "bold"), bg="white", fg="blue")
        year_label.grid(row=1, column=0, padx=10, sticky=W)

        year_combo = ttk.Combobox(current_course_frame, textvariable=self.var_year, font=("Calibri", 10, "bold"), state="readonly")
        year_combo["values"] = ("Select Year", "2021-22", "2022-23", "2023-24", "2024-25")
        year_combo.current(0)
        year_combo.grid(row=1, column=1,  sticky=W)

        # Semester
        sem_label = Label(current_course_frame, text="Semester:", font=("Calibri", 10, "bold"), bg="white", fg="blue")
        sem_label.grid(row=1, column=2, padx=10, sticky=W)

        sem_combo = ttk.Combobox(current_course_frame, textvariable=self.var_semester, font=("Calibri", 10, "bold"), state="readonly")
        sem_combo["values"] = ("Select Semester", "1", "2", "3", "4","5","6","7","8")
        sem_combo.current(0)
        sem_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)
        #
        # Student's Class Information
        #
        student_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Student's Class Information",font=("Calibri", 12, "bold"), fg="green")
        student_frame.place(x=5, y=250, width=720, height=300)

        # studentID
        studentID_label = Label(student_frame, text="StudentID:", font=("Calibri", 10, "bold"), bg="white",fg="blue")
        studentID_label.grid(row=0, column=0, padx=10, sticky=W)

        studentID_entry = ttk.Entry(student_frame, textvariable=self.var_std_id, width=20, font=("Calibri", 10, "bold"))
        studentID_entry.grid(row=0, column=1, padx=10, sticky=W)

        # student's Name
        stdName_label = Label(student_frame, text="Name:", font=("Calibri", 10, "bold"), bg="white",fg="blue")
        stdName_label.grid(row=0, column=2, padx=10, sticky=W)

        stdName_entry = ttk.Entry(student_frame, textvariable=self.var_std_name, width=20, font=("Calibri", 10, "bold"))
        stdName_entry.grid(row=0, column=3, padx=10, sticky=W)

        # class didvision 
        class_div_lable = Label(student_frame, text="Class Division :", font=("Calibri", 10, "bold"), bg="white",fg="blue")
        class_div_lable.grid(row=1, column=0, padx=10, sticky=W)

        gender_combo = ttk.Combobox(student_frame, textvariable=self.var_div, font=("Calibri", 10, "bold"), state="readonly")
        gender_combo["values"] = ("A","B","C")
        gender_combo.current(0)
        gender_combo.grid(row=1, column=1, pady=5, sticky=W)

        # studentRollNo
        studentRoll_label = Label(student_frame, text="Roll No:", font=("Calibri", 10, "bold"), bg="white", fg="blue")
        studentRoll_label.grid(row=1, column=2, padx=10, sticky=W)

        studentRoll_entry = ttk.Entry(student_frame, textvariable=self.var_roll, width=20, font=("Calibri", 10, "bold"))
        studentRoll_entry.grid(row=1, column=3, padx=10, sticky=W)

         # Gender
        gender_label = Label(student_frame, text="Gender:", font=("Calibri", 10, "bold"), bg="white",fg="blue")
        gender_label.grid(row=2, column=0, padx=10, sticky=W)

        gender_combo = ttk.Combobox(student_frame, textvariable=self.var_gender, font=("Calibri", 10, "bold"), state="readonly")
        gender_combo["values"] = ("Male","Female")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1,  pady=5, sticky=W)

        # DOB
        DOB_label = Label(student_frame, text="DOB:", font=("Calibri", 10, "bold"), bg="white", fg="blue")
        DOB_label.grid(row=2, column=2, padx=10, sticky=W)

        DOB_entry = ttk.Entry(student_frame, textvariable=self.var_dob, width=20, font=("Calibri", 10, "bold"))
        DOB_entry.grid(row=2, column=3, padx=10, sticky=W)

        #Email
        Email_label = Label(student_frame, text="Email:", font=("Calibri", 10, "bold"), bg="white",fg="blue")
        Email_label.grid(row=3, column=0, padx=10, sticky=W)

        Email_entry = ttk.Entry(student_frame, textvariable=self.var_email, width=20, font=("Calibri", 10, "bold"))
        Email_entry.grid(row=3, column=1, padx=10, sticky=W)

        # student's Contact Info
        phone_label = Label(student_frame, text="Contact No.:", font=("Calibri", 10, "bold"), bg="white",fg="blue")
        phone_label.grid(row=3, column=2, padx=10, sticky=W)

        phone_entry = ttk.Entry(student_frame, textvariable=self.var_phone, width=20, font=("Calibri", 10, "bold"))
        phone_entry.grid(row=3, column=3, padx=10, sticky=W)

        # student's Address
        address_label = Label(student_frame, text="Address:", font=("Calibri", 10, "bold"), bg="white",fg="blue")
        address_label.grid(row=4, column=0, padx=10, sticky=W)

        address_entry = ttk.Entry(student_frame, textvariable=self.var_address, width=20, font=("Calibri", 10, "bold"))
        address_entry.grid(row=4, column=1,pady=5, padx=10, sticky=W)

        #Teacher name
        Teacher_label = Label(student_frame, text="Teacher Name:", font=("Calibri", 10, "bold"), bg="white",fg="blue")
        Teacher_label.grid(row=4, column=2, padx=10, sticky=W)

        Teacher_entry = ttk.Entry(student_frame, textvariable=self.var_teacher, width=20, font=("Calibri", 10, "bold"))
        Teacher_entry.grid(row=4, column=3,pady=5, padx=10, sticky=W)

        # ==================================Radio Buttons========================================
        self.var_radio1 = StringVar()
        radiobtn1 = ttk.Radiobutton(student_frame, variable=self.var_radio1, text="Capture Photo Sample", value="Yes")
        radiobtn1.grid(row=6, column=0,pady=5,padx=10)

        self.var_radio2 = StringVar()
        radiobtn2 = ttk.Radiobutton(student_frame, variable=self.var_radio1, text="No Photo Sample", value="No")
        radiobtn2.grid(row=6, column=1,pady=5,padx=10)
        # ==================================Buttons Frame========================================
        btnFrame = Frame(student_frame, relief=RIDGE, bg="white")
        btnFrame.place(x=0, y=200, width=715, height=35)

        save_btn = Button(btnFrame, text="Save", command=self.add_data, width=17, font=('arial', 13, 'bold'), bg="red", fg="white")
        save_btn.grid(row=0, column=0)

        update_btn = Button(btnFrame, text="Update",command=self.update_data, width=16, font=('arial', 13, 'bold'), bg="red", fg="white")
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btnFrame, text="Delete",command=self.delete_data, width=16, font=('arial', 13, 'bold'), bg="red", fg="white")
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btnFrame, text="Reset",command=self.reset_data, width=17, font=('arial', 13, 'bold'), bg="red", fg="white")
        reset_btn.grid(row=0, column=3)

        btnFrame1 = Frame(student_frame, relief=RIDGE, bg="white")
        btnFrame1.place(x=0, y=235, width=715, height=35)

        capture_photo_btn = Button(btnFrame1, text="Capture Photo Sample",command=self.generate_dataset, width=34, font=('arial', 13, 'bold'), bg="red", fg="white")
        capture_photo_btn.grid(row=0, column=0)

        update_photo_btn = Button(btnFrame1, text="Update Photo Sample", width=34, font=('arial', 13, 'bold'), bg="red", fg="white")
        update_photo_btn.grid(row=0, column=1)

        # ==================================Search Systems========================================
        search_frame = LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE, text="Search System",font=("Calibri", 12, "bold"), fg="green")
        search_frame.place(x=5, y=60, width=715, height=60)
        
        search_label = Label(search_frame, text=" Search By: ", font=("Calibri", 10, "bold"), bg="blue",fg="white")
        search_label.grid(row=0, column=0, padx=10,pady=5, sticky=W)

        search_combo = ttk.Combobox(search_frame, font=("Calibri", 10, "bold"), state="readonly", width=12)
        search_combo["values"] = ("Select", "Roll_no", "Contact_no", "StdID")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        search_entry = ttk.Entry(search_frame, width=20, font=("Calibri", 10, "bold"))
        search_entry.grid(row=0, column=2, padx=4,pady=5, sticky=W)

        search_btn = Button(search_frame, text="Search", width=10, font=('arial', 10, 'bold'), bg="red", fg="white")
        search_btn.grid(row=0, column=3, padx=4)

        showAll_btn = Button(search_frame, text="Show All",command=self.fetch_data, width=10, font=('arial', 10, 'bold'), bg="red", fg="white")
        showAll_btn.grid(row=0, column=4, padx=4 ,pady=4)

        # ==================================Table Frame==========================================
        table_frame = Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=120, width=720, height=430)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, column=("id", "dep", "course", "year", "semester","name",  "div","roll ","gender",
                                                               "dob",  "email","phone","address","teacher", "photo"),
                                          xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("id", text="StudentID")
        
        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("semester", text="Semester")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("roll ", text="roll in")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("teacher", text="Teather")
        self.student_table.heading("photo", text="PhotoSampleStatus")
        self.student_table["show"] = "headings"

        self.student_table.column("id", width=80)
        self.student_table.column("dep", width=80)
        self.student_table.column("course", width=80)
        self.student_table.column("year", width=80)
        self.student_table.column("semester", width=80)
        self.student_table.column("name", width=80)
        self.student_table.column("gender", width=80)
        self.student_table.column("div", width=80)
        self.student_table.column("roll ", width=80)
        self.student_table.column("dob", width=80)
        self.student_table.column("phone", width=80)
        self.student_table.column("address", width=80)
        self.student_table.column("email", width=80)
        self.student_table.column("teacher", width=80)
        self.student_table.column("photo", width=80)
        self.student_table.pack(fill=BOTH, expand=1)

        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
    # ==================================Functions Declaration========================================
    # =================Add Date========
    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_teacher.get() == "":
            messagebox.showerror("Error", "All Fields are mandatory", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost",username="root",password="",database="FRAS_DB")                                              
                my_cursor = conn.cursor()
                my_cursor.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                  (
                                      self.var_std_id.get(),
                                      self.var_dep.get(),
                                      self.var_course.get(),
                                      self.var_year.get(),
                                      self.var_semester.get(),
                                      self.var_std_name.get(),
                                      self.var_div.get(),
                                      self.var_roll.get(),
                                      self.var_gender.get(),
                                      self.var_dob.get(),
                                      self.var_email.get(),
                                      self.var_phone.get(),
                                      self.var_address.get(),
                                      self.var_teacher.get(),
                                      self.var_radio1.get()
                                  ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Done", "Student details have been added successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)

    #== =======================fetch data  =======
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",
                                               username="root",
                                               password="",
                                               database="fras_db"
                                        )
        my_cursor = conn.cursor()
        my_cursor.execute("select * from students")
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close() 
    #======================== Get cursor ===============
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"] 

        self.var_std_id.set(data[0]),
        self.var_std_name.set(data[5]),
        self.var_dep.set(data[1]),
        self.var_course.set(data[2]),
        self.var_year.set(data[3]),
        self.var_semester.set(data[4]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14]),
    #===================Update
    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" :
            messagebox.showerror("Error", "All Fields are required ", parent=self.root)
        else:
            try:
                update=messagebox.askyesno("update","do you want to update this student details ?", parent=self.root)
                if update>0:
                    conn = mysql.connector.connect(host="localhost",username="root",password="",database="FRAS_DB")                                                                                                                                    
                    my_cursor = conn.cursor()
                    my_cursor.execute("update  students set Dep=%s,course=%s,Year=%s,Semester=%s,name=%s,Gender=%s,Division=%s,Roll=%s,Dob=%s,Email=%s,phone=%s,Address=%s,Teacher=%s,PhotoSample=%s  where student_id=%s ", 
                    (
                                      self.var_dep.get(),
                                      self.var_course.get(),
                                      self.var_year.get(),
                                      self.var_semester.get(),
                                      self.var_std_name.get(),
                                      self.var_gender.get(),
                                      self.var_div.get(),
                                      self.var_roll.get(),
                                      self.var_dob.get(),
                                      self.var_email.get(),
                                      self.var_phone.get(),
                                      self.var_address.get(),
                                      self.var_teacher.get(),
                                      self.var_radio1.get(),
                                      self.var_std_id.get()
                                  ))
                else:
                    if not update:
                        return
                messagebox.showinfo("Success","Student details successflyy update completed.",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
                
    #==============delete data============================
    def delete_data(self):
        if self.var_std_id.get() == "":
            messagebox.showerror("Error", "Student ID Most be Required", parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page ","do you want to Delete this student  ?", parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(host="localhost",
                                               username="root",
                                               password="",
                                               database="FRAS_DB")
                    my_cursor = conn.cursor()
                    sql=("delete from students where Student_id=%s")
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                       return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delet","Student   Delete completed.",parent=self.root)
            except Exception as es:
               messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
                
    #==============Reset ============================   
    def reset_data(self):
         self.var_dep.set("Select Department")
         self.var_course.set("Select Course")
         self.var_year.set("Select Year")
         self.var_semester.set("Select semester")
         self.var_std_id.set("")                            
         self.var_std_name.set("")
         self.var_div.set("")                         
         self.var_roll.set("")                             
         self.var_gender.set("")                            
         self.var_dob.set("")                           
         self.var_email.set("")                             
         self.var_phone.set("")                             
         self.var_address.set("")                             
         self.var_teacher.set("")                             
         self.var_radio1.set("")                                                                                                                                               
    #================== Generate data set or Take photo  ==========
    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" :
            messagebox.showerror("Error", "All Fields are required ", parent=self.root)
        else:
            try:
                conn= mysql.connector.connect(host="localhost",username="root",password="",database="FRAS_DB")                                                                                                                                    
                my_cursor= conn.cursor()
                my_cursor.execute("select * from  students")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                    my_cursor.execute("update  students set Dep=%s,course=%s,year=%s,semester=%s,name=%s,Gender=%s,Division=%s,Roll=%s,Dob=%s,Email=%s,phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where student_id=%s", 
                        (
                                        self.var_std_id.get()==id+1
                                        self.var_dep.get(),
                                        self.var_course.get(),
                                        self.var_year.get(),
                                        self.var_semester.get(),
                                        self.var_std_name.get(),
                                        self.var_div.get(),
                                        self.var_roll.get(),
                                        self.var_gender.get(),
                                        self.var_dob.get(),
                                        self.var_email.get(),
                                        self.var_phone.get(),
                                        self.var_address.get(),
                                        self.var_teacher.get(),
                                        self.var_radio1.get(),
                                    ))
                    conn.commit()
                    self.fetch_data()
                    self.reset_data()
                    conn.close() 

                    #=========load predifiend data on face frontals from opencv=======
                    face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                    def face_cropped(img):
                        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                        faces=face_classifier.detectMultiScale(gray,1.3,5)
                        #scaling factor=1.3
                        #Minimum Neighbor=5

                        for (x,y,w,h) in faces:
                            face_cropped=img[y:y+h,x:x+w]
                            return face_cropped
                    cap=cv2.VideoCapture(0)
                    img_id=0
                    while True:
                        ret,my_frame=cap.read() 
                        if face_cropped(my_frame) is not None:
                            img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)   
                        file_name_path="data_set/user."+str(id)+"."+str(img_id)+".jpg"  
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Crooped Face",face)

                        if cv2.waitKey(1)==13 or int(img_id)==50:
                            break
                    cap.release()
                    cv2.destroyAllWindows()
                    messagebox.showinfo("Result","Generating data sets compled !!!")
            except Exception as es:
                    messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
               
    #=========uplode img======================


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()