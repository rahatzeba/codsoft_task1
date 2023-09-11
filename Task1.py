import tkinter
from tkinter import *
from PIL import ImageTk, Image
root=Tk()
root.title("TO DO LIST ")
root.geometry("368x600")
root.resizable(False,False)

task_list=[]

def addwork():
    task=task_add.get()
    task_add.delete(0,END)

    if task:
        with open("tasklist.txt",'a') as taskfile:
              taskfile.write(f"\n{task}")
        task_list.append(task)
        todoBox.insert(END,task)

def removeWork():
    global task_list
    task=str(todoBox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("tasklist.txt",'w') as taskfile:
            for task in task_list:
                taskfile.write(task+"\n")
        
        todoBox.delete(ANCHOR)
    
def openTaskFile():
       try:
            global task_list
            with open("tasklist.txt","r") as taskfile:
                   tasks=taskfile.readlines()

            for task in tasks:
               if task!="\n":
                task_list.append(task)
                todoBox.insert(END,task)
       except:
          file=open('tasklist.txt','w')
          file.close()
   

#icon
Icon=PhotoImage(file="D:\python\codsoft Internship work\Task1\icon.jpg")
root.iconphoto(False,Icon)

#background_image 
path="D:\python\codsoft Internship work\Task1\Things To-Do.jpg"
img = ImageTk.PhotoImage(Image.open(path))
Label(root,image=img).pack(fill = "both", expand = "no")

#textbox
frame=Frame(root,width=400,height=50,bg="purple")
frame.place(x=0,y=180)
task=StringVar()
task_add=Entry(frame,width=25,font="arial 15 bold",bd=3)
task_add.place(x=10,y=7)
task_add.focus()

button= Button(frame,text="Add", font="arial 15 bold",bg="goldenrod",fg="purple",bd=2,command=addwork)
button.place(x=300,y=5)

#todobox
frame1=Frame(root,bd=4,width=700,height=280,bg="purple")
frame1.place(x=0,y=233)

todoBox=Listbox(frame1,font=('arial',12),width=37,height=16,bg="plum",fg='black',cursor="hand2",selectbackground="indigo")
todoBox.pack(side=LEFT, fill=BOTH,padx=2)
scrollbar=Scrollbar(frame1)
scrollbar.pack(side=RIGHT,fill=BOTH)

todoBox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=todoBox.yview)

openTaskFile()
#delete
DeleteIcon=PhotoImage(file="D:\python\codsoft Internship work\Task1\de.png")
Button(root,image=DeleteIcon,bd=1,command=removeWork).place(x=150,y=555)

root.mainloop()
