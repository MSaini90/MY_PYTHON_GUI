# from tkinter import *

# root = Tk()

# root.geometry("433x533")

# f1 = Frame(root, bg="red" , relief=GROOVE , borderwidth=7 , )
# f1.pack(side=LEFT,fill="y",pady=122)

# f2 = Frame(root, bg="yellow" , relief=SUNKEN , borderwidth=8)
# f2.pack(side=TOP,fill="x")

# f3=Frame(root,borderwidth=8,bg="pink",relief=GROOVE)
# f3.pack(side=RIGHT, fill="y",pady=122)


# l1=Label(f1,text="HEllo")
# l1.pack(pady=243)

# l1=Label(f2, text="Welcome")
# l1.pack()


from tkinter import *  
  
top = Tk()  
top.geometry("140x100")  
frame = Frame(top)  
frame.pack()  
  
leftframe = Frame(top)  
leftframe.pack(side = LEFT)  
  
rightframe = Frame(top)  
rightframe.pack(side = RIGHT)  
  
btn1 = Button(frame, text="Submit", fg="red",activebackground = "red")  
btn1.pack(side = LEFT)  
  
btn2 = Button(frame, text="Remove", fg="brown", activebackground = "brown")  
btn2.pack(side = RIGHT)  
  
btn3 = Button(rightframe, text="Add", fg="blue", activebackground = "blue")  
btn3.pack(side = LEFT)  
  
btn4 = Button(leftframe, text="Modify", fg="black", activebackground = "white")  
btn4.pack(side = RIGHT)  
  
top.mainloop()  

# l=Label(f3, text="Hello")
# l.pack(pady=243)


# root.mainloop()