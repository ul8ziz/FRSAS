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
from Admin_main import *




class Student:
    def __init__(self, root):
        self.root = root 
        swidth= root.winfo_screenwidth() 
        sheight= root.winfo_screenheight()
        self.root.geometry("%dx%d" % (swidth, sheight))
        self.root.title("STUDENT  INFORMATION  MANAGEMENT System")
        self.root.iconbitmap('Images/icon.ico')

        # ==================================variables ========================================
        self.var_dep = StringVar()
        self.var_year = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        # self.var_div=StringVar()
        self.var_search = StringVar()
        self.var_gender = StringVar()
        #self.var_dob= StringVar()
        self.var_email= StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_search_comboo= StringVar()

        

        # background image
        img4 = Image.open("Images/Home.jpg")
        img4 = img4.resize((1600, 1000), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)       

        Frame1 = Frame(root, relief=RIDGE, bg="#063970")
        Frame1.place(x=0, y=0, width=swidth, height=230)
        
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
         
#############
        bg_img = Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=110, width=swidth, height=sheight)
        title_lbl = Label(bg_img, text="STUDENT  INFORMATION  MANAGEMENT SYSTEM ",font=("times new roman", 20, "bold"), bg="white", fg="#063970")
        title_lbl.place(x=0, y=12, width=1600, height=40) 

        main_frame = Frame(bg_img, bd=2)
        main_frame.place(x=10, y=60, width=1500, height=1000)

         # left label frame
        Left_frame = LabelFrame(main_frame, bd=1, relief=RIDGE, text="Student Information", font=("Calibri", 12, "bold"))
        Left_frame.place(x=0, y=0, width=730, height=600)

        img_left = Image.open("Images/grad2.jpg")
        img_left = img_left.resize((720, 130), Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=720, height=130)
       
         # Right label frame
        Right_frame = LabelFrame(main_frame, bd=2,bg="white",relief=RIDGE, text="Student Details", font=("Calibri", 12, "bold"))
        Right_frame.place(x=740, y=10, width=750, height=600)

        img_right = Image.open("Images/grad2.jpg")
        img_right = img_right.resize((730, 130), Image.ANTIALIAS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(Right_frame, image=self.photoimg_right)
        f_lbl.place(x=5, y=0, width=730, height=130)

        #Student's  Information
        student_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student's  Information",font=("Calibri", 12, "bold"), fg="#063970")
        student_frame.place(x=5, y=150, width=720, height=450)

        # studentID
        studentID_label = Label(student_frame, text="StudentID:", font=("Calibri", 10, "bold"), bg="white")
        studentID_label.grid(row=0, column=0, padx=10, sticky=W)

        studentID_entry = ttk.Entry(student_frame, textvariable=self.var_std_id, width=30, font=("Calibri", 10, "bold"))
        studentID_entry.grid(row=0, column=1, padx=10,pady=10, sticky=W)

        # student's Name
        stdName_label = Label(student_frame, text="Name:", font=("Calibri", 10, "bold"), bg="white",)
        stdName_label.grid(row=1, column=0, padx=10, sticky=W,)

        stdName_entry = ttk.Entry(student_frame, textvariable=self.var_std_name, width=30, font=("Calibri", 10, "bold"))
        stdName_entry.grid(row=1, column=1, padx=10, sticky=W)

        # Department
        dep_label = Label(student_frame, text="Department :", font=("Calibri", 10, "bold"), bg="white")
        dep_label.grid(row=2, column=0, padx=10, sticky=W)

        conn = mysql.connector.connect(host="localhost",username="root",password="", database="fras_db"    )
        my_cursor = conn.cursor()
        my_cursor.execute("select Department_name from department")
        depcom=my_cursor.fetchall()
        
        dep_combo = ttk.Combobox(student_frame, textvariable=self.var_dep, font=("Calibri", 10, "bold"), state="readonly")
        dep_combo["values"] = (depcom)
        dep_combo.current(0)
        dep_combo.grid(row=2, column=1, padx=10,pady=10, sticky=W)

        # Year
        year_label = Label(student_frame, text="Year :", font=("Calibri", 10, "bold"), bg="white", )
        year_label.grid(row=3, column=0, padx=10, sticky=W)

        year_combo = ttk.Combobox(student_frame, textvariable=self.var_year, font=("Calibri", 10, "bold"), )
        year_combo["values"] = ("Select Year", "2021-22", "2022-23", "2023-24", "2024-25")
        year_combo.current(0)
        year_combo.grid(row=3, column=1, padx=10, sticky=W)
        #gender
        gender_label = Label(student_frame, text="Gender:", font=("Calibri", 10, "bold"), bg="white",)
        gender_label.grid(row=4, column=0, padx=10, sticky=W)

        gender_combo = ttk.Combobox(student_frame, textvariable=self.var_gender, font=("Calibri", 10, "bold"), state="readonly")
        gender_combo["values"] = ("Male","Female")
        gender_combo.current(0)
        gender_combo.grid(row=4, column=1,  pady=10,padx=10, sticky=W)

        #Email
        Email_label = Label(student_frame, text="Email:", font=("Calibri", 10, "bold"), bg="white")
        Email_label.grid(row=5, column=0, padx=10, sticky=W)

        Email_entry = ttk.Entry(student_frame, textvariable=self.var_email, width=20, font=("Calibri", 10, "bold"))
        Email_entry.grid(row=5, column=1, padx=10,pady=10, sticky=W)

        # student's Contact Info
        phone_label = Label(student_frame, text="Contact No.:", font=("Calibri", 10, "bold"), bg="white")
        phone_label.grid(row=6, column=0, padx=10, sticky=W)

        phone_entry = ttk.Entry(student_frame, textvariable=self.var_phone, width=30, font=("Calibri", 10, "bold"))
        phone_entry.grid(row=6, column=1, padx=10, sticky=W)

        # student's Address
        address_label = Label(student_frame, text="Address:", font=("Calibri", 10, "bold"), bg="white",)
        address_label.grid(row=7, column=0, padx=10, sticky=W)

        address_entry = ttk.Entry(student_frame, textvariable=self.var_address, width=30, font=("Calibri", 10, "bold"))
        address_entry.grid(row=7, column=1,pady=5, padx=10, sticky=W)
        # ==================================Radio Buttons========================================
        self.var_radio1 = StringVar()
        radiobtn1 = ttk.Radiobutton(student_frame, variable=self.var_radio1, text="Capture Photo Sample", value="Yes")
        radiobtn1.grid(row=8, column=0,pady=5,padx=10)

        self.var_radio2 = StringVar()
        radiobtn2 = ttk.Radiobutton(student_frame, variable=self.var_radio1, text="No Photo Sample", value="No")
        radiobtn2.grid(row=8, column=1,pady=5,padx=10)
        # ==================================Buttons Frame========================================
        btnFrame = Frame(student_frame, relief=RIDGE, bg="white")
        btnFrame.place(x=5, y=300, width=710, height=35)

        save_btn = Button(btnFrame, text="Save", command=self.add_data, width=17, font=('arial', 13, 'bold'), bg="#063970", fg="white")
        save_btn.grid(row=0, column=0)

        update_btn = Button(btnFrame, text="Update",command=self.update_data, width=16, font=('arial', 13, 'bold'), bg="#063970", fg="white")
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btnFrame, text="Delete",command=self.delete_data, width=16, font=('arial', 13, 'bold'), bg="#063970", fg="white")
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btnFrame, text="Reset",command=self.reset_data, width=17, font=('arial', 13, 'bold'), bg="#063970", fg="white")
        reset_btn.grid(row=0, column=3)

        btnFrame1 = Frame(student_frame, relief=RIDGE, bg="white")
        btnFrame1.place(x=5, y=340, width=710, height=35)

        capture_photo_btn = Button(btnFrame1, text="Capture Photo Sample",command=self.generate_dataset, width=51, font=('arial', 13, 'bold'), bg="#063970", fg="white")
        capture_photo_btn.grid(row=0, column=0)

        train_btn = Button(btnFrame1, text="Train sample",command=self.generate_dataset, width=17, font=('arial', 13, 'bold'), bg="#063970", fg="white")
        train_btn.grid(row=0, column=2)

        # ==================================Search Systems========================================
        search_frame = LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE, text="Search System",font=("Calibri", 12, "bold"), fg="#063970")
        search_frame.place(x=5, y=60, width=730, height=60)
        
        search_label = Label(search_frame, text=" Search By : ", font=("Calibri", 10, "bold"), bg="white",fg="#063970")
        search_label.grid(row=0, column=0, padx=20,pady=5, sticky=W)

        search_combo = ttk.Combobox(search_frame, font=("Calibri", 10, "bold"),textvariable=self.var_search_comboo, state="readonly", width=10)
        search_combo["values"] = ("Select", "Dep", "Year", "Name","phone")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        search_entry = ttk.Entry(search_frame, width=40,textvariable=self.var_search, font=("Calibri", 10, "bold") )
        search_entry.grid(row=0, column=2, padx=4,pady=5, sticky=W)

        search_btn = Button(search_frame, text="Search", width=10,command=self.search ,font=('arial', 10, 'bold'), bg="#063970", fg="white")
        search_btn.grid(row=0, column=3, padx=4)

        showAll_btn = Button(search_frame, text="Show All",command=self.fetch_data, width=10, font=('arial', 10, 'bold'), bg="#063970", fg="white")
        showAll_btn.grid(row=0, column=4, padx=4 ,pady=4)

        # ==================================Table Frame==========================================
        table_frame = Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=120, width=730, height=450)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, column=("id", "dep", "year","name",  "gender","phone","address","email","photo"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("id", text="StudentID")
        self.student_table.heading("dep", text="Department")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("phone", text="Email")
        self.student_table.heading("address", text="Phone")
        self.student_table.heading("email", text="Address")
        self.student_table.heading("photo", text="PhotoSampleStatus")
        self.student_table["show"] = "headings"

        self.student_table.column("id", width=60)
        self.student_table.column("dep", width=80)
        self.student_table.column("year", width=80)
        self.student_table.column("name", width=80)
        self.student_table.column("gender", width=80)
        self.student_table.column("phone", width=80)
        self.student_table.column("address", width=80)
        self.student_table.column("email", width=80)
        self.student_table.column("photo", width=80)
        self.student_table.pack(fill=BOTH, expand=1)

        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
    # ==================================Functions Declaration========================================
    #######==============search by
    def search(self):
        if self.var_search_comboo.get() == "Select":
                messagebox.showerror("Error", "You Have to selet an item", parent=self.root)
        elif self.var_search_comboo.get() == "Dep":
            
                conn = mysql.connector.connect(host="localhost",username="root",password="",database="FRAS_DB")                                              
                my_cursor = conn.cursor()
                sql=("SELECT * FROM `students` WHERE `Dep`=%s")
                val=(self.var_search.get(),)
                my_cursor.execute(sql,val)
                self.rew=my_cursor.fetchall()
                if len(self.rew)!=0:
                      self.student_table.delete(*self.student_table.get_children())
                      for i in self.rew:
                          self.student_table.insert("",END,values=i)
                      conn.commit()
                conn.close()
        elif self.var_search_comboo.get() == "Year":
            conn = mysql.connector.connect(host="localhost",username="root",password="",database="FRAS_DB")                                              
            my_cursor = conn.cursor()
            sql=("SELECT * FROM `students` WHERE `Year`=%s")
            val=(self.var_search.get(),)
            my_cursor.execute(sql,val)
            self.rew=my_cursor.fetchall()
            if len(self.rew)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in self.rew:
                        self.student_table.insert("",END,values=i)
                    conn.commit()
            conn.close()
        elif self.var_search_comboo.get() == "Name":
            conn = mysql.connector.connect(host="localhost",username="root",password="",database="FRAS_DB")                                              
            my_cursor = conn.cursor()
            sql=("SELECT * FROM `students` WHERE `Name`=%s")
            val=(self.var_search.get(),)
            my_cursor.execute(sql,val)
            self.rew=my_cursor.fetchall()
            if len(self.rew)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in self.rew:
                        self.student_table.insert("",END,values=i)
                    conn.commit()
            conn.close()
        elif self.var_search_comboo.get() == "phone":
            conn = mysql.connector.connect(host="localhost",username="root",password="",database="FRAS_DB")                                              
            my_cursor = conn.cursor()
            sql=("SELECT * FROM `students` WHERE `phone`=%s")
            val=(self.var_search.get(),)
            my_cursor.execute(sql,val)
            self.rew=my_cursor.fetchall()
            if len(self.rew)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in self.rew:
                        self.student_table.insert("",END,values=i)
                    conn.commit()
            conn.close()

    # =================Add student========
    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_gender.get() == "":
            messagebox.showerror("Error", "All Fields are mandatory", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost",username="root",password="",database="FRAS_DB")                                              
                my_cursor = conn.cursor()
                my_cursor.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                  (
                                      self.var_std_id.get(),
                                      self.var_dep.get(),
                                      self.var_year.get(),
                                      self.var_std_name.get(),
                                      self.var_gender.get(),
                                      self.var_email.get(),
                                      self.var_phone.get(),
                                      self.var_address.get(),
                                      self.var_radio1.get()
                                  ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Done", "Student details have been added successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"You have error here:{str(es)}", parent=self.root)

    #== =======================fetch data  =======
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",    username="root",        password="",  database="fras_db"   )
        my_cursor = conn.cursor()
        my_cursor.execute("select * from students ORDER BY `students`.`Student_id` ASC")
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
        self.var_std_name.set(data[3]),
        self.var_dep.set(data[1]),
        self.var_year.set(data[2]),
        self.var_gender.set(data[4]),
        self.var_email.set(data[5]),
        self.var_phone.set(data[6]),
        self.var_address.set(data[7]),
        self.var_radio1.set(data[8]),
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
                    my_cursor.execute("update  students set Dep=%s,Year=%s,name=%s,Gender=%s,Email=%s,phone=%s,Address=%s,PhotoSample=%s  where student_id=%s ", 
                    (                                      
                                      self.var_dep.get(),
                                      self.var_year.get(),
                                      self.var_std_name.get(),
                                      self.var_gender.get(),
                                      self.var_email.get(),
                                      self.var_phone.get(),
                                      self.var_address.get(),
                                      self.var_radio1.get(),
                                      self.var_std_id.get(),
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
               messagebox.showerror("Error",f"here :{str(es)}",parent=self.root)
                
    #==============Reset ============================   
    def reset_data(self):
         self.var_dep.set("Select Department")
         self.var_year.set("Select Year")
         self.var_std_id.set("")                            
         self.var_std_name.set("")             
         self.var_gender.set("Select Gender")                        
         self.var_email.set("")                             
         self.var_phone.set("")                             
         self.var_address.set("")                             
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
                    id=self.var_std_id.get()
                    my_cursor.execute("update  students set Dep=%s,year=%s,name=%s,Gender=%s,Email=%s,phone=%s,Address=%s,PhotoSample=%s where student_id=%s", 
                        (
                                        self.var_std_id.get(),
                                        self.var_dep.get(),
                                        self.var_year.get(),
                                        self.var_std_name.get(),
                                        self.var_gender.get(),
                                        self.var_email.get(),
                                        self.var_phone.get(),
                                        self.var_address.get(),
                                        self.var_radio1.get()
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
                            file_name_path="data_set/face."+str(id)+"."+str(img_id)+".jpg"  
                            cv2.imwrite(file_name_path,face)
                            cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                            cv2.imshow("Crooped Face",face)

                        if cv2.waitKey(1)==20 or int(img_id)==100:
                            break
                    cap.release()
                    cv2.destroyAllWindows()
                    messagebox.showinfo("Result","Generating data sets compled !!!")
            except Exception as es:
                    messagebox.showerror("Error",f"You have error here :{str(es)}",parent=self.root)
               
    #========= home======================
    def home(self):
        self.root.withdraw()
        self.new_window = Toplevel(self.root)
        b = Admin_main(self.new_window)  
        
    def exite(self):
             self.exit=messagebox.askyesno("FRSAS"," Are you sure exit this project ?",parent=self.root)
             if self.exit >0:
                  self.root.destroy()
             else:
                  return



if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()