# from tkinter import *
# _saini_root=Tk()
# _saini_root.geometry("455x244")
# photo=PhotoImage(file="moh.png")
# ms_lable=Label(image=photo)

# ms_lable.pack()
# _saini_root.mainloop()


# for jpg image
from tkinter import *
from PIL import Image, ImageTk  # ImageTk Function Help for taking jpg file in tkinter
_saini_root=Tk()
_saini_root.geometry("455x244")

image=Image.open("MYFS.jpg")
photo=ImageTk.PhotoImage(image)
ms_lable=Label(image=photo)

ms_lable.pack()
_saini_root.mainloop()
