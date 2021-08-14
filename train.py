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

        title_lbl = Label(self.root, text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("arial", 35, "bold"), bg="white", fg="#063970")
        title_lbl.place(x=0, y=0, width=1530, height=45) 

        # first image
        img1 = Image.open("Images/OIP.jpeg")
        img1 = img1.resize((1530, 325), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=0, y=55, width=1530, height=325)

       #button
        Butt = Button(self.root, text="Train Data", command=self.train_classifier, cursor="hand2", font=("times new roman",25, "bold"),bg="#063970", fg="white")
        Butt.place(x=0, y=380, width=1530, height=60)

        # second image
        img2 = Image.open("Images/OIP.jpeg")
        img2 = img2.resize((1530, 325), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=0, y=440, width=1530, height=325)
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
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = train(root)
    root.mainloop()