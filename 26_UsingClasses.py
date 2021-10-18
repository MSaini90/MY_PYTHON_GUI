from tkinter import *

class GUI(Tk):
	def __init__(self):   #Here Root has been removed by self in this class
		super().__init__()
		self.geometry("344x344")

  
	def click (self):
		print("Button clicked") 

  
	def createbutton(self, inptext):
			Button(text = inptext, command= self.click).pack()

	def status(self):
			self.var = StringVar()
			self.var.set("Ready")
			self.statusbar = Label(self, textvar = self.var, 
			relief = SUNKEN,anchor = "w")
			self.statusbar.pack(side = BOTTOM, fill = X)

if __name__ == '__main__':
	window = GUI()  
	window.status()    
	window.createbutton("click me")   #Here Window has taken the place of root 
	window.mainloop()




root.mainloop()