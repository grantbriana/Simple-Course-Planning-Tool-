import tkinter as tk
import os
#import Simple_Course_Planning_Tool

#Setup Tkinter
root = tk.Tk()

#Window creation.
root.title("Simple Course Planning Tool")
canvas = tk.Canvas(root, width = 500, height = 200, bg = "#263D42")
canvas.pack()

#function for the Name Button to call when clicked.
def Submit():
    name = nameInput.get()
    showName = tk.Label(root, text = name)
    canvas.create_window(400, 100, window = showName)
    path = pathMenu.get()
    pathLabel = tk.Label(root, text = path)
    canvas.create_window(400, 150, window = pathLabel)

#Textbox to type user's name into.
nameEntryLabel = tk.Label(root, text = "Enter the name of the Student", fg = "white", bg = "red")
canvas.create_window(250, 80, window = nameEntryLabel)
nameInput = tk.Entry(root)
canvas.create_window(250, 100, window = nameInput)

#Button to submit input
submitButton = tk.Button(root, text ="Submit", padx=10, pady = 4, fg ="white", bg ="blue", command = Submit)
submitButton.pack()

#drop menu for selecting a path.
pathMenu = tk.StringVar()
pathMenu.set("Select your degree Path:")
drop = tk.OptionMenu(root, pathMenu, "Software Systems", "Game Development", "Network Security")
drop.pack()

root.mainloop()

