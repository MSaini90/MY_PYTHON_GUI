from tkinter import *

root = Tk()

root.geometry("655x500")

root.title("Notepad")

def MyFunc():
	print("I am feeling something sad now")


# These two widget are used for created a non drop drown menu
# mymenu= Menu(root)
# mymenu.add_command(label="File", command=MyFunc)
# mymenu.add_command(label="Exit", command=quit)
# root.config(menu=mymenu)

filemenu=Menu(root)
m1=Menu(filemenu , tearoff=0)
m1.add_command(label="New" , command=MyFunc)
m1.add_command(label="New Window", command=MyFunc) 
m1.add_command(label="Open" , command=MyFunc)
m1.add_command(label="Save" , command=MyFunc)
m1.add_command(label="Save As" , command=MyFunc)
m1.add_command(label="Page Setup" , command=MyFunc)
m1.add_command(label="Print" , command=MyFunc)
m1.add_separator() # It's used for add separator in the subenu
m1.add_command(label="Exit" , command = quit)
root.config( menu=filemenu)
filemenu.add_cascade(label="File",menu=m1) #add_casecade it's used for add submenues in main menu



m2=Menu(filemenu , tearoff=0)
m2.add_command(label="Undo" , command=MyFunc)
m2.add_command(label="Cut", command=MyFunc) 
m2.add_command(label="Copy" , command=MyFunc)
m2.add_command(label="Paste" , command=MyFunc)
m2.add_command(label="Delete" , command=MyFunc)
m2.add_command(label="Search with Bing" , command=MyFunc)
m2.add_command(label="Find" , command=MyFunc)
m2.add_command(label="Fing Next" ,command=MyFunc)
m2.add_command(label="Fing Previous" ,command=MyFunc)
m2.add_command(label="Replace" ,command=MyFunc)
m2.add_command(label="Go To" ,command=MyFunc)
m2.add_command(label="Select All" ,command=MyFunc)
m2.add_command(label="Date/Time" ,command=MyFunc)
root.config(menu=filemenu)
filemenu.add_cascade(label="Edit", menu=m2)



m3=Menu(filemenu , tearoff=0)
m3.add_command(label="Word Wrap" , command=MyFunc)
m3.add_command(label="Font", command=MyFunc) 
root.config( menu=filemenu)
filemenu.add_cascade(label="Format", menu=m3)

m4=Menu(filemenu , tearoff=0)
m4.add_command(label="Zoom" , command=MyFunc)
m4.add_command(label="Status Bar", command=MyFunc) 
root.config( menu=filemenu)
filemenu.add_cascade(label="View", menu=m4)

m5=Menu(filemenu , tearoff=0)
m5.add_command(label="View Help" , command=MyFunc)
m5.add_command(label="Send Feedback", command=MyFunc) 
m5.add_command(label="About Notepad" , command=MyFunc)
root.config(menu=filemenu)
filemenu.add_cascade(label="Help", menu=m5)




root.mainloop()