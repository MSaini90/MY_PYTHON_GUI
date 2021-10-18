from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

if __name__ == '__main__':
	#Basic tkinter setup
	root = Tk()
	root.title("Untitled - Notepad")
	# root.wm_iconbitmap("1.ico")
	root.geometry("655x788")


		#Add Textarea 
	TextArea = Text(root, font = "Consolas 11")
	file = None  #It will target none file before open
	TextArea.pack(expand = True, fill = BOTH)
  #End textarea from here

  #Adding scrollbar form here 
	Scroll = Scrollbar(TextArea)
	Scroll.pack(side = RIGHT, fill = Y)
	Scroll.config(command = TextArea.yview)
	TextArea.config(yscrollcommand = Scroll.set)
  #End scrollbar from here

  #Creating function from here
	def newFile():
		global file
		msb = askyesnocancel("Notepad", "Do you want to save changes to Untitled")
		print(msb)
		
		if msb == True:
      saveFile()


    else:
      root.title("Untitled - Notepad")
			file = None	
			TextArea.delete(1.0, END)  #Delete  function is available in the TextArea
				

	def openFile():
		global file
		msb = askyesnocancel("Notepad", "Do you want to save changes to Untitled")
		print(msb)
		if msb == True:
			saveFile()

		file = askopenfilename(defaultextension = ".txt",filetypes = [("All Files", "*.*"), ("Text Documents", "*.text")])
		if file == "":
			file = None
		else:
			root.title(os.path.basename(file) + " - Notepad")
			TextArea.delete(1.0, END)
			f = open (file, "r")
			TextArea.insert(1.0 ,f.read())
			f.close()

	def saveFile():
		global file
		if file == None:
			file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension = ".txt",filetypes = [("All Files", "*.*"), ("Text Documents", "*.text")])
			if file == "":
					file = None

			else:
				#Save as a new file 
				f = open(file, "w")
				f.write(TextArea.get(1.0 , END))
				f.close()
				root.title(os.path.basename(file)+ " - Notepad")
		
		else:
			#save the file
			f = open(file ,"w")
			f.write(TextArea.get(1.0, END))
			f.close()




	def quitApp():
		msb = askyesnocancel("Notepad", "Do you want to save changes to Untitled")
		print(msb)
		if msb == True:
			saveFile()
		root.destroy()

	

	def cut():
		TextArea.event_generate("<<Cut>>")
		
	def copy():
		TextArea.event_generate("<<Copy>>")

	def paste():
		TextArea.event_generate("<<Paste>>")

	def about():
		showinfo("Notepad" , "Notepad by Mohit Saini")



	#Lets create a MenuBar
	MenuBar = Menu(root)
	
  #FileMenu Starts from here
	FileMenu = Menu(MenuBar, tearoff = 0)
	#To open new file 
	FileMenu.add_command(label = "New", command = newFile)
	
	FileMenu.add_command(label = "Open", command = openFile)
	FileMenu.add_command(label = "Save", command = saveFile)
	FileMenu.add_separator()
	FileMenu.add_command(label = "Exit", command = quitApp)
	MenuBar.add_cascade(label = "File", menu = FileMenu)
	root.config(menu = MenuBar)
	#FileMenu ends from here

	#Edit Menu Starts 
	EditMenu = Menu(MenuBar, tearoff=0)
  # TO give a features of cut, copy, paste
	EditMenu.add_command(label = "Cut", command = cut)
	EditMenu.add_command(label = "Copy" , command = copy)
	EditMenu.add_command(label = "Paste", command = paste)
	MenuBar.add_cascade(label = "Edit", menu = EditMenu)
	root.config(menu = MenuBar)
	# Edit Menu Ends Form here 

	#Help Menu starts from here
	HelpMenu = Menu(MenuBar , tearoff= 0)
	HelpMenu.add_command(label = "About Notepad" , command = about)
	MenuBar.add_cascade(label = "Help", menu = HelpMenu)
	#Help Menu Ends from here


	root.config(menu = MenuBar)
	root.mainloop()