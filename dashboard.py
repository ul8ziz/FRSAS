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

class dashboard:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1600x900+0+0")
        self.root.title("Admin Control")

        #################varbales
        self.var_depp = StringVar()
        self.var_tracher = StringVar()
        
        #============Department frame================
        department_frame = LabelFrame(self.root, bd=2, bg="white", relief=RIDGE, text="Department Information",font=("Calibri", 13, "bold"), fg="green")
        department_frame.place(x=5, y=100, width=720, height=250)
        
        #Department entry
        department_label = Label(department_frame, text="New Department :", font=("Calibri", 10, "bold"), bg="white",fg="blue")
        department_label.grid(row=0, column=0,pady=0, padx=20, sticky=W)

        department_entry = ttk.Entry(department_frame, width=20,textvariable=self.var_depp, font=("Calibri", 10, "bold"))
        department_entry.grid(row=0, column=1,pady=30, padx=0, sticky=W)

        save_btn = Button(department_frame, text="Save", command=self.add_dep, width=15, font=('arial', 11, 'bold'), bg="red", fg="white")
        save_btn.grid(row=2, column=0)
        
        update_btn = Button(department_frame, text="Update",command=self.fetch_data, width=15, font=('arial', 11, 'bold'), bg="red", fg="white")
        update_btn.grid(row=2, column=1)

        delete_btn = Button(department_frame, text="Delete", command=self.delete_dep,width=15, font=('arial', 11, 'bold'), bg="red", fg="white")
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
        Tracher_frame = LabelFrame(self.root, bd=2, bg="white", relief=RIDGE, text="Tracher Information",font=("Calibri", 13, "bold"), fg="green")
        Tracher_frame.place(x=5, y=400, width=720, height=250)
        
        #Tracher entry
        Tracher_label = Label(Tracher_frame, text="New Tracher :", font=("Calibri", 10, "bold"), bg="white",fg="blue")
        Tracher_label.grid(row=0, column=0,pady=0, padx=30, sticky=W)

        Tracher_entry = ttk.Entry(Tracher_frame, width=20,textvariable=self.var_tracher, font=("Calibri", 10, "bold"))
        Tracher_entry.grid(row=0, column=1,pady=30, padx=0, sticky=W)

        save_btn = Button(Tracher_frame, text="Save", command=self.add_tracher, width=15, font=('arial', 11, 'bold'), bg="red", fg="white")
        save_btn.grid(row=2, column=0)
        
        update_btn = Button(Tracher_frame, text="Update",command=self.fetch_Tracher, width=15, font=('arial', 11, 'bold'), bg="red", fg="white")
        update_btn.grid(row=2, column=1)

        delete_btn = Button(Tracher_frame, text="Delete", command=self.delete_Tracher,width=15, font=('arial', 11, 'bold'), bg="red", fg="white")
        delete_btn.grid(row=2, column=2)

        # =======Table Frame
        table__frame = Frame(Tracher_frame, bd=2, bg="white", relief=RIDGE)
        table__frame.place(x=450, y=0, width=250, height=220)

        scroll_x = ttk.Scrollbar(table__frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table__frame, orient=VERTICAL)

        self.Tracher_table_frame = ttk.Treeview(table__frame, column=("id", "Tracher"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Tracher_table_frame.xview)
        scroll_y.config(command=self.Tracher_table_frame.yview)

        self.Tracher_table_frame.heading("id", text="Tracher ID")
        
        self.Tracher_table_frame.heading("Tracher", text="Tracher Name")
        self.Tracher_table_frame["show"] = "headings"

        self.Tracher_table_frame.column("id", width=70)
        self.Tracher_table_frame.column("Tracher", width=100)
        self.Tracher_table_frame.pack(fill=BOTH, expand=1)

        self.Tracher_table_frame.bind("<ButtonRelease>",self.get_Tracher_cursor)
        self.fetch_Tracher()

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

        #add new  Tracher  
    #++++++++++++++++++++++++  add teacher
    def add_tracher(self):
        if self.var_depp.get() == "Select Tracher" or self.var_tracher.get() == "" :
            messagebox.showerror("Error", "The Field empty", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost",username="root",password="",database="FRAS_DB")                                              
                my_cursor = conn.cursor()
                my_cursor.execute("insert into Tracher (Tracher_name) values(%s)",
                                  (
                                      self.var_tracher.get(),
                                  ))
                conn.commit()
                conn.close()
                self.fetch_data()
                messagebox.showinfo("Done", "Tracher have been added successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)

    #== =======================fetch  Tracher =======
    def fetch_Tracher(self):
        conn = mysql.connector.connect(host="localhost",
                                               username="root",
                                               password="",
                                               database="fras_db"
                                        )
        my_cursor = conn.cursor()
        my_cursor.execute("select * from Tracher")
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
                    query="DELETE FROM  Tracher WHERE Tracher_name=%s"
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
    
        self.var_depp.set(data[1])
        self.var_depp.set(data[1])
        self.var_depp.set(data[1])
   #======================== Get cursor Tracher ===============
    def get_Tracher_cursor(self,event=""):
        cursor_focus=self.Tracher_table_frame.focus()
        content=self.Tracher_table_frame.item(cursor_focus)
        data=content["values"] 
        self.var_tracher.set(data[1])




if __name__ == "__main__":
    root = Tk()
    obj = dashboard(root)
    root.mainloop()



