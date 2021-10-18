from tkinter import *

def getvalue():
	# There are two function in python's tkinter's variabeclass  
	# 1 - get() It's used for getting value
	# 2 - set() It's used for Setting value 

	print("It works")
	print(f"{namevalue.get() , phonevalue.get() , gendervalue.get() , emergencyvalue.get() , paymentmodevalue.get() , foodservicevalue.get()}")
	
	with open("records.txt","a") as f:
		f.write(f"{namevalue.get() , phonevalue.get() , gendervalue.get() , emergencyvalue.get() , paymentmodevalue.get() , foodservicevalue.get()}\n")
root=Tk()

root.geometry("644x533")

Label(root, text="Welcome to Mohit Travels", pady=6, font="comicsansns 13 bold").grid(row=0, column=3)

name=Label(root, text="Name")
phone=Label(root, text="Phone")
gender=Label(root, text="gender")
emergency=Label(root, text="Emergency Contact")
paymentmode=Label(root, text="Payment Mode")

# Pack text in our form
name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
emergency.grid(row=4, column=2)
paymentmode.grid(row=5, column=2)

# Tkinter variable for storing values 
namevalue=StringVar() # Variale class
phonevalue=StringVar()
gendervalue=StringVar()
emergencyvalue=StringVar()
paymentmodevalue=StringVar()
foodservicevalue=StringVar()

# Entries for our form
nameentry=Entry(root, textvariable=namevalue)
phoneentry=Entry(root, textvariable=phonevalue)
genderentry=Entry(root, textvariable=gendervalue)
emergencyentry=Entry(root, textvariable=emergencyvalue)
paymentmodeentry=Entry(root, textvariable=paymentmodevalue)

# packing the Entries
nameentry.grid(row="1",column=3)
phoneentry.grid(row="2",column=3)
genderentry.grid(row="3",column=3)
emergencyentry.grid(row="4",column=3)
paymentmodeentry.grid(row="5",column=3)

# Checks box
foodservice=Checkbutton(text="Want to prebook your meals", variable=foodservicevalue)
foodservice.grid(row=6,column=3)

Button(text="Submit to Mohit Travels", command=getvalue,relief=GROOVE).grid(row=7,column=3)
root.mainloop()