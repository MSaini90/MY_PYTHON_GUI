from tkinter import *
root = Tk()
root.title("Listbox")
root.geometry("222x223")

def add():
	global i
	lbx.insert(ACTIVE, f"{i}")
	# i+=1
i = "Mohit"


lbx = Listbox(root)
lbx.pack()
lbx.insert(END, "First item of list box")

Button(root, text = "Add Item", command=add).pack()
btn= Button(root, text = "delete", command = lambda lbx=lbx: lbx.delete(ANCHOR)).pack(anchor = "e",fill = X)
root.mainloop()