# import cv2

# #print("Before URL")
# cap = cv2.VideoCapture('http://192.168.1.20:4747')
# #print("After URL")

#     while True:

#         #print('About to start the Read command')
#         ret, frame = cap.read()
#         #print('About to show frame of Video.')
#         cv2.imshow("Capturing",frame)
#         #print('Running..')

#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     cap.release()
#     cv2.destroyAllWindows()

import tkinter as tk
import datetime
import time

 
app = tk.Tk() 
app.geometry('300x200')
app.title("Basic Status Bar")

statusbar = tk.Label(app, text="on the way…", bd=1, relief=tk.SUNKEN, anchor=tk.W)
statusbar.pack(side=tk.BOTTOM, fill=tk.X)

global key
key = ''
ts = time.time()
date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
day,month,year=date.split("-")
mont={'01':'January',
    '02':'February',
    '03':'March',
    '04':'April',
    '05':'May',
    '06':'June',
    '07':'July',
    '08':'August',
    '09':'September',
    '10':'October',
    '11':'November',
    '12':'December'
    }

lbl = tk.Label(app, text=day+"-"+mont[month]+"-"+year+"  |  ",width=20  ,height=1  ,fg="black"  ,bg="#00aeff" ,font=('times', 17, ' bold ') )
lbl.place(x=33, y=55)

tv= tk.Treeview(app,height =13,columns = ('name','date','time'))
tv.column('#0',width=82)
tv.column('name',width=130)
tv.column('date',width=133)
tv.column('time',width=133)
tv.grid(row=2,column=0,padx=(0,0),pady=(150,0),columnspan=4)
tv.heading('#0',text ='ID')
tv.heading('name',text ='NAME')
tv.heading('date',text ='DATE')
tv.heading('time',text ='TIME')


app.mainloop()