import tkinter as tk
import os
import webbrowser
from tkinter import filedialog as fd

root = tk.Tk()

#Window creation.
root.title("Simple Course Planning Tool (v2) Beta")
canvas = tk.Canvas(root, width = 500, height = 200, bg = "#263D42")
canvas.pack()
#filePath = tk.StringVar()


#function for the Name Button to call when clicked.
def Submit():
    name = nameInput.get()
    showName = tk.Label(root, text = name)
    canvas.create_window(400, 100, window = showName)
    path = pathMenu.get()
    pathLabel = tk.Label(root, text = path)
    canvas.create_window(400, 150, window = pathLabel)
    root.quit()
    root.destroy()

#Textbox to type user's name into.
nameEntryLabel = tk.Label(root, text = "Enter the name of the Student", fg = "white", bg = "red")
canvas.create_window(250, 80, window = nameEntryLabel)
nameInput = tk.Entry(root)
canvas.create_window(250, 100, window = nameInput)

filePath = tk.StringVar()

def degreeWorksPath():
    #filePath = tk.StringVar()
    filename = fd.askopenfilename()
    filePath.set(filename)
    #canvas.create_window(250, 120, window = filePath)

#Button to submit input'
degreeWorksButton = tk.Button(root, text ="DegreeWorks Path", padx=10, pady = 4, fg ="white", bg ="blue", command = degreeWorksPath)
submitButton = tk.Button(root, text ="Submit", padx=15, pady = 9, fg ="white", bg ="blue", command = Submit)
submitButton.pack()
degreeWorksButton.pack()


#drop menu for selecting a path.
pathMenu = tk.StringVar()
pathMenu.set("Select your degree track:")
drop = tk.OptionMenu(root, pathMenu, "Software Systems", "Game Development", "Network Security", "Education", "Web Development", "Enterprise")
drop.pack()

def chatbot():
    webbrowser.open_new_tab('webChat.html')


chatbotButton = tk.Button(root, text ="Chat Assistant", padx=20, pady = 12, fg ="white", bg ="blue", command = chatbot)
chatbotButton.pack()

submitButton.pack()


root.mainloop()