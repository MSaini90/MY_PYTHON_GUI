from tkinter import *

root=Tk()

canvas_width=400
canvas_height=800

root.geometry(f"{canvas_width}x{canvas_height}")

can_widget=Canvas(root, width=canvas_width , height=canvas_height)

can_widget.pack()

# The line goes from the point x1, y1 to x2, y2
can_widget.create_line(0,0,800,400, fill = "red")
can_widget.create_line(0,400,800,0, fill = "red")

# To cerate a rectangle specify parameters in this order 
# 1 = Coors of top LEFT
# 2 = coors of the BOTTOM right

# can_widget.create_rectangle(3,5, 700, 300, fill = "red")
can_widget.create_text(200,200 , text = "Python")
can_widget.create_oval(344,233,244,355)
root.mainloop()