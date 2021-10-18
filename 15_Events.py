from tkinter import *

def Mohit(event):
	print(f"You clicked on the button at {event.x} , {event.y} ")

root=Tk()

root.title("Events in tkinter")
root.geometry("644x334")

widget=Button(root, text="Click me")
widget.pack()
widget.bind('<Button-1>' , Mohit)
widget.bind('<Double-1>' , quit)
root.mainloop()