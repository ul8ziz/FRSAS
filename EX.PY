import tkinter as tk
 
app = tk.Tk() 
app.geometry('300x200')
app.title("Basic Status Bar")


menubar = tk.Menu(app)

filemenu = tk.Menu(menubar)
filemenu.add_command(label="Open")
filemenu.add_command(label="Save")
filemenu.add_command(label="Exit")

menubar.add_cascade(label="File", menu=filemenu)

statusbar = tk.Label(app, text="on the way…", bd=1, relief=tk.SUNKEN, anchor=tk.W)
statusbar.pack(side=tk.BOTTOM, fill=tk.X)
app.mainloop()