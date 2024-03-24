import tkinter
import tkinter.font

# Window Settings
window = tkinter.Tk()
window.title("Todo List")
window.geometry("250x400+0+0")
window.resizable(False, False)

titleLabel = tkinter.Label(window, text = "TODO LIST", font = tkinter.font.Font(family = "BMDoHyeon-OTF", size = 30), height = 2)
listbox = tkinter.Listbox(window, height = 10, selectmode = "browse")
inputTextField = tkinter.Entry(width = 20)

# Functions of Action of Buttons
def addThings():
	if inputTextField.get() is not "":
		listbox.insert(0, inputTextField.get())
		inputTextField.delete(0, "end")
		
def deleteThings():
	if(listbox.curselection() is not ()): 
		print(listbox.curselection()) # Testing whether it's working...
		listbox.delete(listbox.curselection())
	
	
addButton = tkinter.Button(window, overrelief = "solid", width = 15, command = addThings, text = "추가하기")
deleteButton = tkinter.Button(window, overrelief = "solid", width = 15, command = deleteThings, text = "완료하기")

# Packing Widgets
titleLabel.pack()
inputTextField.pack()
addButton.pack()
deleteButton.pack()
listbox.pack()

# Window Completion
window.mainloop()