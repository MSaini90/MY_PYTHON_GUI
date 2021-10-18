from tkinter import *
root = Tk()
root.title("Scrollbar")
# For connecting scrollbar to a Widget
# 1 . widget(yscrollcommand = Scrollbar.set)
#2. scrollbar.config(command=widget.yview)

scrollbar = Scrollbar(root)
scrollbar.pack(side = RIGHT ,fill = Y)


lbx = Listbox(root,yscrollcommand = scrollbar.set)

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@For number purpose @@@@@@@@@@@@@@@@@@@@@@@@@@
# for i in range(344):
# 	lbx.insert(END,f"Item{i}")
# lbx.pack(fill = "both",padx = 22)
# scrollbar.config(command=lbx.yview)

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ For text purpose 
text = Text(root, yscrollcommand = scrollbar.set)
text.pack(fill = "both")
scrollbar.config(command=text.yview)


root.mainloop()