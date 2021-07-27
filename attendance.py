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
import csv
from tkinter import filedialog
import os

mydata=[]
class attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1600x900+0+0")
        self.root.title("FRAS")

        #=================varaibles
        self.var_id = StringVar()
        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_time = StringVar()
        self.var_date = StringVar()
        self.var_dep = StringVar()
        self.var_attendance = StringVar()

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
        main_frame.place(x=20, y=55, width=1480, height=600)

        # left label frame
        Left_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Attendance Details", font=("Calibri", 12, "bold"))
        Left_frame.place(x=10, y=10, width=730, height=580)

        img_left = Image.open("Images/student.jpg")
        img_left = img_left.resize((720, 130), Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=720, height=130)

        in_Left_frame = LabelFrame(Left_frame, bd=2, relief=RIDGE,bg="white")
        in_Left_frame.place(x=0, y=135, width=720, height=300)

        #entrys

        # studentID
        studentID_label = Label(in_Left_frame, text="StudentID:", font=("Calibri", 10, "bold"), bg="white")
        studentID_label.grid(row=0, column=0, padx=20,pady=5, sticky=W)

        studentID_entry = ttk.Entry(in_Left_frame, textvariable=self.var_id, width=20, font=("Calibri", 10, "bold"))
        studentID_entry.grid(row=0, column=1, padx=10,pady=5, sticky=W)

        # student's Name
        stdName_label = Label(in_Left_frame, text="Name:", font=("Calibri", 10, "bold"), bg="white",)
        stdName_label.grid(row=0, column=2, padx=20,pady=5, sticky=W)

        stdName_entry = ttk.Entry(in_Left_frame,textvariable=self.var_name,  width=20, font=("Calibri", 10, "bold"))
        stdName_entry.grid(row=0, column=3, padx=10,pady=5, sticky=W)
        # Department
        dep_label = Label(in_Left_frame, text="Department :", font=("Calibri", 10, "bold"), bg="white", )
        dep_label.grid(row=1, column=0, padx=20,pady=5, sticky=W)

        dep_combo = ttk.Combobox(in_Left_frame, textvariable=self.var_dep, font=("Calibri", 10, "bold"), state="readonly")
        dep_combo["values"] = ("Select Department", "cs", "IT", "Electronics", "Civil")
        dep_combo.current(0)
        dep_combo.grid(row=1, column=1, pady=5, sticky=W)

        # Course
        course_label = Label(in_Left_frame, text="roll :", font=("Calibri", 10, "bold"), bg="white", )
        course_label.grid(row=1, column=2, padx=20,pady=5, sticky=W)

        course_combo = ttk.Combobox(in_Left_frame,textvariable=self.var_roll, font=("Calibri", 10, "bold"), state="readonly")
        course_combo["values"] = ("Select Course", "C++", "Jave", "php", "web", "A+")
        course_combo.current(0)
        course_combo.grid(row=1, column=3, pady=5, sticky=W)

        # time
        time_label = Label(in_Left_frame, text="Time:", font=("Calibri", 10, "bold"), bg="white")
        time_label.grid(row=2, column=0, padx=20,pady=5, sticky=W)

        time_entry = ttk.Entry(in_Left_frame,  width=20,textvariable=self.var_time, font=("Calibri", 10, "bold"))
        time_entry.grid(row=2, column=1, padx=10,pady=5, sticky=W)

        # date
        date_label = Label(in_Left_frame, text="Date:", font=("Calibri", 10, "bold"), bg="white")
        date_label.grid(row=2, column=2, padx=20,pady=5, sticky=W)

        date_entry = ttk.Entry(in_Left_frame,  width=20, textvariable=self.var_date,font=("Calibri", 10, "bold"))
        date_entry.grid(row=2, column=3, padx=10,pady=5, sticky=W)
        # Status
        Status_label = Label(in_Left_frame, text="Status :", font=("Calibri", 10, "bold"), bg="white")
        Status_label.grid(row=3, column=0, padx=20, pady=5,sticky=W)

        Status_combo = ttk.Combobox(in_Left_frame, textvariable=self.var_attendance, font=("Calibri", 10, "bold"), state="readonly")
        Status_combo["values"] = (" ", "Present","Upsent")
        Status_combo.current(0)
        Status_combo.grid(row=3, column=1,  pady=5,sticky=W)
        
        #buttons frame 
        btnFrame = Frame(in_Left_frame, relief=RIDGE, bg="white")
        btnFrame.place(x=0, y=200, width=715, height=35)

        save_btn = Button(btnFrame, text="Import csv",command=self.importCsv, width=17, font=('arial', 13, 'bold'), bg="blue", fg="white")
        save_btn.grid(row=0, column=0)

        update_btn = Button(btnFrame, text="Export csv",command=self.exportcsv, width=17, font=('arial', 13, 'bold'), bg="blue", fg="white")
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btnFrame, text="Update", width=17, font=('arial', 13, 'bold'), bg="blue", fg="white")
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btnFrame, text="Reset", command=self.reset_data, width=17, font=('arial', 13, 'bold'), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3)


        # Right label frame
        Right_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Attendance Details", font=("Calibri", 12, "bold"))
        Right_frame.place(x=750, y=10, width=730, height=580)

        table_Frame = Frame(Right_frame, relief=RIDGE, bg="white")
        table_Frame.place(x=5, y=5, width=700, height=455)

        scroll_x = ttk.Scrollbar(table_Frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_Frame, orient=VERTICAL)

        self.AttendaceReport_table = ttk.Treeview(table_Frame,
         column=("id", "name", "roll" , "Dep","Time","Date", "Attendance"),
         xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.AttendaceReport_table.xview)
        scroll_y.config(command=self.AttendaceReport_table.yview)

        self.AttendaceReport_table.heading("id", text="StudentID")
        self.AttendaceReport_table.heading("name", text="Name")
        self.AttendaceReport_table.heading("roll", text="roll")
        self.AttendaceReport_table.heading("Dep", text="Dep")
        self.AttendaceReport_table.heading("Time", text="Time")
        self.AttendaceReport_table.heading("Date", text="Date")
        self.AttendaceReport_table.heading("Attendance", text="Attendance")
        self.AttendaceReport_table["show"] = "headings"

        self.AttendaceReport_table.column("id", width=80)
        self.AttendaceReport_table.column("name", width=100)
        self.AttendaceReport_table.column("roll", width=100)
        self.AttendaceReport_table.column("Dep", width=100)
        self.AttendaceReport_table.column("Time", width=80)
        self.AttendaceReport_table.column("Date", width=100)
        self.AttendaceReport_table.column("Attendance", width=100)
        self.AttendaceReport_table.pack(fill=BOTH, expand=1)

        self.AttendaceReport_table.bind("<ButtonRelease>",self.get_cursor)
        #===========Funcation ==============
        
    def fetchData(self,rows):
        self.AttendaceReport_table.delete(*self.AttendaceReport_table.get_children())
        for i in rows:
            self.AttendaceReport_table.insert("",END,values=i)
    # importCsv
    def importCsv(self):
        # try: 
            global mydata
            mydata.clear()
            fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("csv file","*.csv"),("All File","*.*")),parent=self.root)            
            with open(fln) as myfile:
                csvread=csv.reader(myfile,delimiter=",")
                for  i in csvread:
                    mydata.append(i)
            self.fetchData(mydata)

        # except Exception as es:
        #         messagebox.showerror("Error", f"{str(es)}", parent=self.root)

    # export csv
    def exportcsv(self):
       
            if len(mydata)<1:
              messagebox.showerror("No Data","No Data found to export ",parent=self.root)
              return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)            
            with open (fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                   exp_write.writerow(i)
                messagebox.showinfo("Date Export","Your data exported to "+os.path.basename(fln)+"successfully")
        
    #get cursor
    def get_cursor(self,event=""):
        cursor_row=self.AttendaceReport_table.focus()
        content=self.AttendaceReport_table.item(cursor_row)
        rows=content["values"] 
        self.var_id.set(rows[0]),
        self.var_name.set(rows[1]),
        self.var_roll.set(rows[2]),
        self.var_dep.set(rows[3]),
        self.var_time.set(rows[4]),
        self.var_date.set(rows[5]),
        self.var_attendance.set(rows[6])
    #reset
    def reset_data(self):
        self.var_id.set(""),
        self.var_name.set(""),
        self.var_dep.set(""),
        self.var_roll.set(""),
        self.var_time.set(""),
        self.var_date.set(""),
        self.var_attendance.set(""),



        









if __name__ == "__main__":
    root = Tk()
    obj = attendance(root)
    root.mainloop()