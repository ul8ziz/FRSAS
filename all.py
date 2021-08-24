# Developer :ul8ziZ
# Date : 7-12 2021

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import os

from student import *
from train import train
from dashboard import dashboard
from face_recognition import face_recognition
from attendance import attendance




class all:
    def __init__(self, root):
        self.root = root
        swidth= root.winfo_screenwidth() 
        sheight= root.winfo_screenheight()
        self.root.geometry("%dx%d" % (swidth, sheight))
        self.root.title("About the System")
        self.root.iconbitmap('Images/icon.ico')

        
       

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
    
  
    

if __name__ == "__main__":
    root = Tk()
    obj = all(root)
    root.mainloop()

