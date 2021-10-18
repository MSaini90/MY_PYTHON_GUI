from tkinter import *
import  tkinter.messagebox as tmsg

root = Tk()
root.title("Radiobutton")
root.geometry("377x437")


def order():
	tmsg.showinfo("Order Received", f"We have received your order for {var.get()}  thanks for ordering")

var = StringVar()
var.set("Radio")
Label(root , text ="What would you like to have sir?" , font = "lucida 18 bold",
      justify = LEFT, padx = 14).pack()

radio = Radiobutton(root, text = "Dosa", padx= 14, variable=var, value = "Dosa").pack(
      	anchor = "w")
radio = Radiobutton(root, text = "Idly", padx= 14, variable=var, value = "Idly").pack(
      	anchor = "w")
radio = Radiobutton(root, text = "Samosa", padx= 14, variable=var, value = "Samosa").pack(
      	anchor = "w")

Button(text = "Oreder now", command= order).pack()
root.mainloop()


