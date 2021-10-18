from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.geometry("455x344")
root.title("Slider tutorial")


def getdollar():
	print(f"We have credited {myslider2.get()} dollars to your bank account")
	tmsg.showinfo("Amount credited",f"We have credited {myslider2.get()} dollars to your bank account")
# myslider = Scale(root , from_ = 0 , to = 100)
# myslider.pack()

Label(root, text = "How many dollars do you want?").pack()
myslider2 = Scale(root, from_ = 0, to=100,orient=HORIZONTAL, tickinterval = 50) #Tickinterval tells about Interval difference between slider
myslider2.set(34)  #Initial value
myslider2.pack()

Button(root, text = "GET dollars",pady = 10, command = getdollar).pack()
root.mainloop()