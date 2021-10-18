

# Important Lable Options
# |||||||||||||||||||||||
# text : for adds the text
# bd : background
# fg : foreground
# font : sets the font
# 1-font : ("comicsansms", 14, "bold")
# 2-font : "comicsansms 14 bold"
# padx : x padding
# pady : y padding
# relief-border styling- SUNKEN, RAISED, GROOVE, RIDGE

# Important Pack options
# ||||||||||||||||||||||
# anchor=nw
# side=top,bottom, left,right
# fill
# padx
# pady


from tkinter import *
root=Tk()

root.geometry("560x450")
root.title("Notepad")

title_label=Label(text="""Musk was born to a Canadian mother and South African
 \nfather and raised in Pretoria, South Africa. He briefly attended the University
 \nof Pretoria before moving to Canada when he was 17 to attend Queen's University.
 \nHe transferred to th. Musk then founded X.com, an online bank. It merged with
 \nConfinity in 2000, which had launched PayPal the
 \nprevious year and was subsequently bought by eBay for $1.5 billion in October 
 2002.""",bg="Orange",fg="white" ,padx=33,pady=87, font="comicsansms 14 bold" , borderwidth=5, 
 relief=SUNKEN)

# title_label.pack(side=TOP , anchor="se")
# title_label.pack(side=LEFT,fill=Y)                 

# title_label.pack(side=LEFT,fill=Y,padx=34,pady=34)
root.mainloop()