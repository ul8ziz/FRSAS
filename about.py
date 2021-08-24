# Developer :ul8ziZ
# Date : 7-12 2021

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
from Admin_main import *

class about:
    def __init__(self, root):
        self.root = root
        swidth= root.winfo_screenwidth() 
        sheight= root.winfo_screenheight()
        self.root.geometry("%dx%d" % (swidth, sheight))
        self.root.title("About the System")
        self.root.iconbitmap('Images/icon.ico')

        
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
        
    # =================================== Functions =========================================

  
    def home(self):
        self.root.withdraw()
        self.new_window = Toplevel(self.root)
        bp = Admin_main(self.new_window)  
        
    def exite(self):
             self.exit=messagebox.askyesno("FRSAS"," Are you sure exit this project ?",parent=self.root)
             if self.exit >0:
                  self.root.destroy()
             else:
                  return

if __name__ == "__main__":
    root = Tk()
    obj = about(root)
    root.mainloop()

