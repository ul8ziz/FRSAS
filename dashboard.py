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
from register import *
from Admin_main import *



class dashboard:
    def __init__(self, root):
        self.root = root
        swidth= root.winfo_screenwidth() 
        sheight= root.winfo_screenheight()
        self.root.geometry("%dx%d" % (swidth, sheight))
        self.root.title("Admin Control")
        self.root.config(bg = '#154c79')
        self.root.iconbitmap('Images/icon.ico')
        #self.root.wm_attributes('-transparentcolor','#add123')

        img4 = Image.open("Images/home.jpg")
        img4 = img4.resize((swidth,sheight), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bg_img = Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=0, width=swidth, height=sheight)
        #################varbales
        self.var_depp = StringVar()
        self.var_tracher = StringVar()
        self.var_cources = StringVar()
        self.var_courcesid = StringVar()


        
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

        #============Department frame================
        department_frame = LabelFrame(self.root, bd=2, bg="white", relief=RIDGE,text="Department Information",font=("Calibri", 13, "bold"), fg="#063970")
        department_frame.place(x=5, y=120, width=720, height=210)
        
        #Department entry
        department_label = Label(department_frame, text="New Department :", font=("Calibri", 10, "bold"), bg="white")
        department_label.grid(row=0, column=0,pady=0, padx=20, sticky=W)

        department_entry = ttk.Entry(department_frame, width=20,textvariable=self.var_depp, font=("Calibri", 10, "bold"))
        department_entry.grid(row=0, column=1,pady=30, padx=0, sticky=W)

        save_btn = Button(department_frame, text="Save", command=self.add_dep, width=15, font=('arial', 11, 'bold'), bg="#063970", fg="white")
        save_btn.grid(row=2, column=0)
        
        update_btn = Button(department_frame, text="Update",command=self.fetch_data, width=15, font=('arial', 11, 'bold'), bg="#063970", fg="white")
        update_btn.grid(row=2, column=1)

        delete_btn = Button(department_frame, text="Delete", command=self.delete_dep,width=15, font=('arial', 11, 'bold'), bg="#063970", fg="white")
        delete_btn.grid(row=2, column=2)

        # =======Table Frame
        table_frame = Frame(department_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=450, y=0, width=250, height=200)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.Department_table = ttk.Treeview(table_frame, column=("id", "dep"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Department_table.xview)
        scroll_y.config(command=self.Department_table.yview)

        self.Department_table.heading("id", text="Department ID")
        
        self.Department_table.heading("dep", text="Department Name")
        self.Department_table["show"] = "headings"

        self.Department_table.column("id", width=70)
        self.Department_table.column("dep", width=100)
        self.Department_table.pack(fill=BOTH, expand=1)

        self.Department_table.bind("<ButtonRelease>",self.get_department_cursor)
        self.fetch_data()

 #============Tracher_frame==============================================================================================================
        Tracher_frame = LabelFrame(self.root, bd=2, bg="white", relief=RIDGE, text="Tracher Information",font=("Calibri", 13, "bold"), fg="#063970")
        Tracher_frame.place(x=5, y=337, width=720, height=230)
        
        #Tracher entry
        Tracher_label = Label(Tracher_frame, text="New Tracher :", font=("Calibri", 10, "bold"), bg="white")
        Tracher_label.grid(row=0, column=0,pady=0, padx=30, sticky=W)

        Tracher_entry = ttk.Entry(Tracher_frame, width=20,textvariable=self.var_tracher, font=("Calibri", 10, "bold"))
        Tracher_entry.grid(row=0, column=1,pady=20, padx=0, sticky=W)
        self.var_type = StringVar()

        type = Label(Tracher_frame, text="Type :", font=("Calibri", 10, "bold"), bg="white")
        type.grid(row=1, column=0,pady=0, padx=30, sticky=W)

        self.combo_security_Q = ttk.Combobox(Tracher_frame,textvariable=self.var_type,width=12, font=(   "times new roman", 10, "bold"), state="readonly")
        self.combo_security_Q["values"] = (            "Select", "Admin", "Teacher")
        self.combo_security_Q.grid(row=1, column=1,pady=0, padx=0, sticky=W)

        
        
        update_btn = Button(Tracher_frame, text="Update",command=self.teacher_update, width=15, font=('arial', 11, 'bold'), bg="#063970", fg="white")
        update_btn.grid(row=2, column=1)

        delete_btn = Button(Tracher_frame, text="Delete", command=self.delete_Tracher,width=15, font=('arial', 11, 'bold'), bg="#063970", fg="white")
        delete_btn.grid(row=2, column=2)

        add_new_tea_btn = Button(Tracher_frame, text="Add New Teacher",command=self.new_teaher, width=15, font=('arial', 11, 'bold'), bg="#063970", fg="white")
        add_new_tea_btn.grid(row=2, column=0,pady=10)


        # =======Table Frame
        table__frame = Frame(Tracher_frame, bd=2, bg="white", relief=RIDGE)
        table__frame.place(x=450, y=0, width=250, height=220)

        scroll_x = ttk.Scrollbar(table__frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table__frame, orient=VERTICAL)

        self.Tracher_table_frame = ttk.Treeview(table__frame, column=("id", "Tracher","type"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Tracher_table_frame.xview)
        scroll_y.config(command=self.Tracher_table_frame.yview)

        self.Tracher_table_frame.heading("id", text="ID")
        
        self.Tracher_table_frame.heading("Tracher", text="Tracher Name")
        self.Tracher_table_frame.heading("type", text="type")
        self.Tracher_table_frame["show"] = "headings"

        self.Tracher_table_frame.column("id", width=40)
        self.Tracher_table_frame.column("Tracher", width=100)
        self.Tracher_table_frame.column("type", width=100)
        self.Tracher_table_frame.pack(fill=BOTH, expand=1)

        self.Tracher_table_frame.bind("<ButtonRelease>",self.get_Tracher_cursor)
        self.fetch_Tracher()


        ###################cources
         #============cources frame================
        cources_frame = LabelFrame(self.root, bd=2, bg="white", relief=RIDGE,text="cources Information",font=("Calibri", 13, "bold"), fg="#063970")
        cources_frame.place(x=5, y=580, width=720, height=220)
        
        #cources entry
        departmentid_label = Label(cources_frame, text=" id :", font=("Calibri", 10, "bold"), bg="white")
        departmentid_label.grid(row=0, column=0,pady=10, padx=20, sticky=W)

        id_entry = ttk.Entry(cources_frame, width=20,textvariable=self.var_courcesid, font=("Calibri", 10, "bold"))
        id_entry.grid(row=0, column=1,pady=10, padx=0, sticky=W)
 
        department_label = Label(cources_frame, text="New cources :", font=("Calibri", 10, "bold"), bg="white")
        department_label.grid(row=1, column=0,pady=0, padx=20, sticky=W)

        department_entry = ttk.Entry(cources_frame, width=20,textvariable=self.var_cources, font=("Calibri", 10, "bold"))
        department_entry.grid(row=1, column=1,pady=5, padx=0, sticky=W)


        save_btn = Button(cources_frame, text="Save", command=self.add_cources, width=15, font=('arial', 11, 'bold'), bg="#063970", fg="white")
        save_btn.grid(row=2, column=0)
        
        update_btn = Button(cources_frame, text="Update",command=self.fetch_course_data, width=15, font=('arial', 11, 'bold'), bg="#063970", fg="white")
        update_btn.grid(row=2, column=1)

        delete_btn = Button(cources_frame, text="Delete", command=self.delete_course,width=15, font=('arial', 11, 'bold'), bg="#063970", fg="white")
        delete_btn.grid(row=2, column=2)

        # =======cources Table 
        table_cources = Frame(cources_frame, bd=2, bg="white", relief=RIDGE)
        table_cources.place(x=450, y=0, width=250, height=200)

        scroll_x = ttk.Scrollbar(table_cources, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_cources, orient=VERTICAL)

        self.cources_table = ttk.Treeview(table_cources, column=("id", "course"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.cources_table.xview)
        scroll_y.config(command=self.cources_table.yview)

        self.cources_table.heading("id", text="id")
        self.cources_table.heading("course", text="course")
        self.cources_table["show"] = "headings"

        self.cources_table.column("id", width=70)
        self.cources_table.column("course", width=100)
        self.cources_table.pack(fill=BOTH, expand=1)

        self.cources_table.bind("<ButtonRelease>",self.get_var_cources_cursor)
        self.fetch_course_data()


        #======================Fun
    #add new  Department  
    def add_dep(self):
        if self.var_depp.get() == "Select Department" or self.var_depp.get() == "" :
            messagebox.showerror("Error", "The Field empty", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost",username="root",password="",database="FRAS_DB")                                              
                my_cursor = conn.cursor()
                my_cursor.execute("insert into department (Department_name) values(%s)",
                                  (
                                      self.var_depp.get(),
                                  ))
                conn.commit()
                conn.close()
                self.fetch_Tracher()
                messagebox.showinfo("Done", "Department have been added successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)
    
    #==============delete department============================
    def delete_dep(self):
        if self.var_depp.get() == "":
            messagebox.showerror("Error", "Department Most be Required", parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Department Delete Page ","do you want to Delete this Department  ?", parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(host="localhost",username="root", password="",database="FRAS_DB")
                    my_cursor = conn.cursor()
                    query="DELETE FROM  department WHERE Department_name=%s"
                    val=(self.var_depp.get(),)
                    my_cursor.execute(query,val)                  
                else:
                    if not delete:
                       return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delet","deparment   Delete completed.",parent=self.root)
            except Exception as es:
               messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
    
    #== =======================fetch data department =======
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",
                                               username="root",
                                               password="",
                                               database="fras_db"
                                        )
        my_cursor = conn.cursor()
        my_cursor.execute("select * from department")
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.Department_table.delete(*self.Department_table.get_children())
            for i in data:
                self.Department_table.insert("",END,values=i)
            conn.commit()
        conn.close() 
    #======================== Get cursor department ===============
    def get_department_cursor(self,event=""):
        cursor_focus=self.Department_table.focus()
        content=self.Department_table.item(cursor_focus)
        data=content["values"] 
        self.var_depp.set(data[1])
    ######################################cources
    #== =======================fetch data cources =======
    def fetch_course_data(self):
        conn = mysql.connector.connect(host="localhost",
                                               username="root",
                                               password="",
                                               database="fras_db"
                                        )
        my_cursor = conn.cursor()
        my_cursor.execute("select * from courses")
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.cources_table.delete(*self.cources_table.get_children())
            for i in data:
                self.cources_table.insert("",END,values=i)
            conn.commit()
        conn.close() 
     #add new  cources  
    def add_cources(self):
        if self.var_cources.get() == "Select courses" or self.var_cources.get() == "" :
            messagebox.showerror("Error", "The Field empty", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost",username="root",password="",database="FRAS_DB")                                              
                my_cursor = conn.cursor()
                my_cursor.execute("insert into courses (course_id,course_name) values(%s,%s)",
                                  (                                        
                                      self.var_courcesid.get(),
                                      self.var_cources.get(),
                                  ))
                conn.commit()
                conn.close()
                self.fetch_course_data()
                messagebox.showinfo("Done", "course have been added successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)
    #==============delete cources============================
    def delete_course(self):
        if self.var_courcesid.get() == "":
            messagebox.showerror("Error", "id Most be Required", parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("course Delete Page ","do you want to Delete this course  ?", parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(host="localhost",username="root", password="",database="FRAS_DB")
                    my_cursor = conn.cursor()
                    query="DELETE FROM  courses WHERE course_id=%s"
                    val=(self.var_courcesid.get(),)
                    my_cursor.execute(query,val)                  
                else:
                    if not delete:
                           return
                conn.commit()
                self.fetch_course_data()
                conn.close()
                messagebox.showinfo("Delet","course   Delete completed.",parent=self.root)
            except Exception as es:
               messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
    
    #======================== Get cursor cources ===============
    def get_var_cources_cursor(self,event=""):
        cursor_focus=self.cources_table.focus()
        content=self.cources_table.item(cursor_focus)
        data=content["values"] 
        self.var_courcesid.set(data[0])
        self.var_cources.set(data[1])

        #add new  Tracher  
    #++++++++++++++++++++++++  add teacher
    # def add_tracher(self):
    #     if self.var_depp.get() == "Select teacher" or self.var_tracher.get() == "" :
    #         messagebox.showerror("Error", "The Field empty", parent=self.root)
    #     else:
    #         try:
    #             conn = mysql.connector.connect(host="localhost",username="root",password="",database="FRAS_DB")                                              
    #             my_cursor = conn.cursor()
    #             my_cursor.execute("insert into teacher (teacher_name) values(%s)",
    #                               (
    #                                   self.var_tracher.get(),
    #                               ))
    #             conn.commit()
    #             conn.close()
    #             self.fetch_data()
    #             messagebox.showinfo("Done", "teacher have been added successfully", parent=self.root)
    #         except Exception as es:
    #             messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)

    #== =======================fetch  Tracher =======
    def fetch_Tracher(self):
        conn = mysql.connector.connect(host="localhost",
                                               username="root",
                                               password="",
                                               database="fras_db"
                                        )
        my_cursor = conn.cursor()
        my_cursor.execute("select Teacher_id,Teacher_name,type from teacher")
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.Tracher_table_frame.delete(*self.Tracher_table_frame.get_children())
            for i in data:
                self.Tracher_table_frame.insert("",END,values=i)
            conn.commit()
        conn.close() 
    #==============delete Tracher============================
    def delete_Tracher(self):
        if self.var_tracher.get() == "":
            messagebox.showerror("Error", "Tracher Most be Required", parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Tracher Delete Page ","do you want to Delete this Tracher  ?", parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(host="localhost",username="root", password="",database="FRAS_DB")
                    my_cursor = conn.cursor()
                    query="DELETE FROM  teacher WHERE teacher_name=%s"
                    val=(self.var_tracher.get(),)
                    my_cursor.execute(query,val)                  
                else:
                    if not delete:
                       return
                conn.commit()
                self.fetch_Tracher()
                conn.close()
                messagebox.showinfo("Delet","Tracher   Delete completed.",parent=self.root)
            except Exception as es:
               messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
    
        

         #==============delete Tracher============================
    
   #======================== Get cursor Tracher ===============
    def get_Tracher_cursor(self,event=""):
        cursor_focus=self.Tracher_table_frame.focus()
        content=self.Tracher_table_frame.item(cursor_focus)
        data=content["values"] 
        self.var_tracher.set(data[1]        )
        self.var_type.set(data[2]        )

       
    def teacher_update(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="",database="FRAS_DB")                                                                                                                                    
        my_cursor = conn.cursor()
        my_cursor.execute("update  teacher set type=%s where teacher_name=%s ", 
        (                                      
                            self.var_type.get(),
                            self.var_tracher.get(),

                            
                                  ))
        conn.commit()
        conn.close()
        messagebox.showinfo("update","teacher   update completed.",parent=self.root)

        self.fetch_Tracher()

    #========= home======================
    def home(self):
            self.root.withdraw()
            self.new_window = Toplevel(self.root)
            dd = Admin_main(self.new_window)

    def exite(self):
             self.exit=messagebox.askyesno("FRSAS"," Are you sure exit this project ?",parent=self.root)
             if self.exit >0:
                  self.root.destroy()
             else:
                  return 
    def new_teaher(self):
            self.root.withdraw()
            self.new_window = Toplevel(self.root)
            bb = Register(self.new_window)




if __name__ == "__main__":
    root = Tk()
    obj = dashboard(root)
    root.mainloop()



