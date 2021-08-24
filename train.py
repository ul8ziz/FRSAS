# Developer :ul8ziZ
# Date : 7-12 2021

from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import os
import numpy as np
import cv2





class train:
    def __init__(self, root):
        self.root = root
        swidth= root.winfo_screenwidth() 
        sheight= root.winfo_screenheight()
        self.root.geometry("%dx%d" % (swidth, sheight))
        self.root.title("Train Data")
        img4 = Image.open("Images/home.jpg")
        img4 = img4.resize((swidth,sheight), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        self.root.iconbitmap('Images/icon.ico')

        bg_img = Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=0, width=swidth, height=sheight)

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
        
        #button
        Butt = Button(self.root, text="Train Data", command=self.train_classifier, cursor="hand2", font=("times new roman",25, "bold"),bg="#063970", fg="white")
        Butt.place(x=540, y=300, width=400, height=60)

        #=================================training ==================
    def train_classifier(self):
        try:
            data_dir=("data_set")
            path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
            faces=[]
            ids=[]
            for image in path:
                img=Image.open(image).convert('L')
                imageNp=np.array(img,'uint8')
                id=int(os.path.split(image)[1].split('.')[1])
                faces.append(imageNp)
                ids.append(id)
                cv2.imshow("Training",imageNp)
                cv2.waitKey(1)==13
            ids=np.array(ids)
            #==============Train the classifier And save ========
            clf=cv2.face.LBPHFaceRecognizer_create() 
            clf.train(faces,ids)
            clf.write("classifier.xml")
            cv2.destroyAllWindows()
            messagebox.showinfo("Result","Training datasets Completed !")
        except Exception as es:
                messagebox.showerror("Error", f"errer in:{str(es)}", parent=self.root)
    #========= home======================
    def home(self):
             self.new_window = Toplevel(self.root)
             self.app =Admin_main(self.new_window)

    def exite(self):
             self.exit=messagebox.askyesno("FRSAS"," Are you sure exit this project ?",parent=self.root)
             if self.exit >0:
                  self.root.destroy()
             else:
                  return 



if __name__ == "__main__":
    root = Tk()
    obj = train(root)
    root.mainloop()