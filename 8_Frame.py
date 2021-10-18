from tkinter import *
root= Tk()

root.geometry("633x333")

f1=Frame(root,bg="grey",borderwidth=6,relief=RAISED)
f1.pack(side=LEFT, fill="y",pady=122)

f2=Frame(root,borderwidth=8,bg="red",relief=GROOVE)
f2.pack(side=TOP, fill="x")


l=Label(f1, text="Project TKinter")
l.pack(pady=200)

l=Label(f2, text="Project PYGAME",font="Helvetica 16 bold",fg="red",pady=22)
l.pack()


root.mainloop()