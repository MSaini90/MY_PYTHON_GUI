from tkinter import *

def getvalue():
	f=open("MohitFirstGUI.txt","a")
	username=str(uservalue.get())
	password=str(passvalue.get())
	f.write("Username is : " +username+"\n")
	f.write("Password is : "+password+"\n")
	print("Successfully Entered")

def Checkvalues():
	try:
		with open("MohitFirstGUI.txt","r") as file:
			values=file.read()
			print(values)
	except:
		print("Sorry! data is not available")

def updataValues():
	try:
		with open("MohitFirstGUI.txt","r") as file:
			values=file.read()
	except:

		print("Sorry! data is not available")
	
	passupdate=input("Enter new password for updation=")
	userupdate=input("Enter new username for updation=")
  

		
root=Tk()

root.geometry("323x324")

user=Label(root,text="Username")
password=Label(root,text="Password")

user.grid()
password.grid(row=1)

uservalue=StringVar()
passvalue=StringVar()

userentry=Entry(root, textvariable=uservalue)
passentry=Entry(root, textvariable=passvalue)

userentry.grid(row=0,column=1)
passentry.grid(row=1,column=1)

Button(text="Submit", command=getvalue).grid()
Button(text="Check", command=Checkvalues).grid()    
Button(text="Update",command=updataValues).grid()                           #

root.mainloop()