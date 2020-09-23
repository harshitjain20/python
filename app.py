from tkinter import *
import os
import tkinter.filedialog
root = Tk()
apps = []

if os.path.isfile("save.txt"):
    with open("save.txt","r") as f:
        tempApp = f.read()
        tempApp = tempApp.split(',')
        apps = [x for x in tempApp if x.strip()]
        print(apps)

def addApp():
    for widget in fram.winfo_children():
        widget.destroy()
    fileName = tkinter.filedialog.askopenfilename(initialdir="/",title="Select exe file",
                                              filetypes=(("executables","*.exe"),("all files","*.*")))
    apps.append(fileName)
    # print(fileName.name)
    for app in apps:
        l = Label(fram,text=app,bg="gray")
        l.pack()

def runApps():
    for app in apps:
        os.startfile(app)

canvas = Canvas(root,height=500,width=500,bg="#263D42")
canvas.pack()
fram = Frame(root,bg="white")
fram.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)
openFileBtn = Button(root,text="Open File",padx=10,pady=5,fg="white",bg="#263D42",command=addApp)
openFileBtn.pack()
runAppBtn = Button(root,text="Run Apps",padx=10,pady=5,fg="white",bg="#263D42",command= runApps)
runAppBtn.pack()

for a in apps:
    lb = Label(fram,text=a)
    lb.pack()

root.mainloop()
with open("save.txt","a") as f:
    for app in apps:
        f.write(app+",")