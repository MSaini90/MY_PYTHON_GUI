from tkinter import *
root = Tk()
root.geometry("566x566")

root.title("My custom GUI")

# root.wm_iconbitmap("i.ico")
root.configure(background = "grey")

width = root.winfo_screenwidth()
                                   #both used For getting screen size
height = root.winfo_screenheight()
print(f"{width}x{height}")
Button(text = "Close", command = root.destroy).pack()

root.mainloop()