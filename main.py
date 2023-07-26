import tkinter
from tkinter import *
from PIL import ImageTk,Image



root = Tk()
image_0 = Image.open('bgf.png')
bck_end = ImageTk.PhotoImage(image_0)
root.geometry("400x600")
backgroundd = Label(root,image=bck_end)
backgroundd.place(x=0,y=0)
root.title("CheckMaro")
root.resizable(False,False)

task_list = []

def addTask():
    task = task_entry.get()
    task_entry.delete(0,END)

    if task:
        with open("tasklist.txt","a") as taskfile:
            taskfile.write(f"\n{task}")
        
        task_list.append(task)
        listbox.insert(END,task)
def deleteTask():
    global task_list
    task = str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("tasklist.txt","w") as taskfile:
            for  task in task_list:
                taskfile.write(task+'\n')

        listbox.delete(ANCHOR)




def opentaskfile():
    try:
        with open("tasklist.txt","r") as taskfile:
            tasks = taskfile.readlines()

        for task in tasks:
            if task !='\n':
                task_list.append(task)
                listbox.insert(END,task)

    except:
        file = open('tasklist.txt','w')
        file.close





#main
frame = Frame(root,width=400,height= 45,bg="#fff")
frame.place(x=25,y=140)

task = StringVar()
task_entry = Entry(frame,width=20,font="verdana 15",fg="#000",bd=1,bg="#fff")
task_entry.place(x=10,y=0)
task_entry.focus()

#Button
button = Button(frame,bg="#219617",text="Add",fg="#fff",width=5,height=1,command=addTask)
button.place(x=290,y=0)

#List box

frame1 = Frame(root,bd=1,bg="#fff",width=300,height=300).place(x=35,y=200)

listbox = Listbox(frame1,font=("verdana",15),width=20,height=13,bg="#f5faf5",fg="#000",cursor="hand2",selectbackground="#d6d6d6")
listbox.place(x=35,y=200)

scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT,fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)
opentaskfile()

#delete
#Del_icon=PhotoImage(file="del3.png")
button = Button(root,bg="#fa0505",width=2,command=deleteTask,fg="#fff",text="X",font="Aerial 10").place(x=330,y=350)


root.mainloop()
