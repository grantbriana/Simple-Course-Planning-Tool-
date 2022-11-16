# import tkinter as tk
# import os
# from tkinter import filedialog as fd
# from tkinter import ttk
#
# root = tk.Tk()
#
# #Window creation.
# screen_width = root.winfo_screenwidth()
# screen_height = root.winfo_screenheight()
# center_width = screen_width/2
# center_height = screen_height/2
# root.title("Simple Course Planning Tool")
# canvas = tk.Canvas(root, width = screen_width, height = screen_height, bg = "#263D42")
# canvas.pack()
# #root.attributes('-fullscreen', True)
# #filePath = tk.StringVar()
#
#
# #function for the Name Button to call when clicked.
# def Submit():
#     name = nameInput.get()
#     showName = tk.Label(root, text = name)
#     canvas.create_window(400, 100, window = showName)
#     path = pathMenu.get()
#     pathLabel = tk.Label(root, text = path)
#     canvas.create_window(400, 150, window = pathLabel)
#     root.quit()
#     root.destroy()
#
# #Textbox to type user's name into.
# nameEntryLabel = tk.Label(root, text = "Enter the name of the Student", fg = "white", bg = "red", font=("Arial", 25))
# canvas.create_window(center_width, 80, window = nameEntryLabel)
# nameInput = tk.Entry(root, width=75)
# canvas.create_window(center_width, 135, window = nameInput)
#
# filePath = tk.StringVar()
#
# def degreeWorksPath():
#     #filePath = tk.StringVar()
#     filename = fd.askopenfilename()
#     filePath.set(filename)
#     #canvas.create_window(250, 120, window = filePath)
#
# #Button to submit input'
# degreeWorksButton = tk.Button(root, text ="DegreeWorks Path", padx=70, pady = 40, fg ="white", bg ="blue", font=("Arial", 20), command = degreeWorksPath)
# submitButton = tk.Button(root, text ="Submit", padx=150, pady = 40, fg ="white", bg ="blue",font=("Arial", 20), command = Submit)
# submitButton.place(x=(center_width - 150), y=700)
# degreeWorksButton.place(x=(center_width - 150), y=590)
#
#
# #drop menu for selecting a path.
# pathMenu = tk.StringVar()
# pathMenu.set("Select your degree track:")
# drop = ttk.Combobox(root, width=50, height=1000, textvariable=pathMenu, font=("Arial", 30))
# drop['values'] = ("Software Systems", "Game Development", "Network Security", "Education", "Web Development", "Enterprise")
# #drop.grid(column=1,row=15)
# drop.current(1)
# drop.place(x=(center_width - 300), y=500)
#
#
#
# root.mainloop()
#!/usr/bin/python3
#!/usr/bin/python3
import csv
import pathlib
import pygubu
import tkinter as tk
import os
from tkinter import filedialog as fd, ttk

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI =  "C:/Users/archa/Desktop/version 0.2/SCPToolUi/SCPToolUi.ui"


class NewprojectApp:


    def __init__(self, master=None):
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        # Main widget
        self.mainwindow = builder.get_object("frame1", master)
        builder.connect_callbacks(self)
        current_var = tk.StringVar()
        self.trackCombo = builder.get_object('TrackCombo')
        self.nameInput = builder.get_object('nameInput')
        self.ClassList = builder.get_object('CourseList')
        self.DesiredHours = builder.get_object('entry2')
        options = ("Software Systems", "Game Development", "Network Security", "Education", "Web Development", "Enterprise")
        self.trackCombo['values'] = options
        self.trackCombo['state'] = 'readonly'
        self.nameInput.insert(0,'Enter Name')
        self.DesiredHours.insert(0,'12')
        self.DegreeWork = tk.StringVar()

    def run(self):
        self.mainwindow.mainloop()

    def degreeWorksPath(self):
        filePath = tk.StringVar()
        filename = fd.askopenfilename()
        filePath.set(filename)
        self.DegreeWork.set(filename)
    def DegreeWork(self):
        return self.DegreeWork()


    def classAdd(self, data):
        self.ClassList.insert(tk.END,data)

    def populateCourseArray(self, path):
        # relevant spreadsheet opened
        if os.path.isfile(path):
            with open(path, 'r') as csvfile:
                datareader = csv.reader(csvfile)
                # row[6] (prerequisites) iterated and added to prereq. list
                app.ClassList.delete(0, tk.END)
                for row in datareader:
                    prereq = row[7].split(",")
                    self.classAdd(row[1])
        else:
            app.ClassList.delete(0,tk.END)

    def trackCallBack(self, drop):
        match drop:
            # software systems
            case "Software Systems":
                course_requirements = "C:\SCP_Tool\Software Systems Track.csv"
                self.populateCourseArray(course_requirements)
            # education
            case "Education":
                course_requirements = "version 0.2\Tracks\Education Track.csv"
                self.populateCourseArray(course_requirements)
            # cybersecurity
            case "Network Security":
                course_requirements = "version 0.2\Tracks\Cybersecurity Track.csv"
                self.populateCourseArray(course_requirements)
            # games programming
            case "Game Development":
                course_requirements = "version 0.2\Tracks\Games Programming Track.csv"
                self.populateCourseArray(course_requirements)
            # web development
            case "Web Development":
                course_requirements = "version 0.2\web development track.csv"
                self.populateCourseArray(course_requirements)
            # Enterprise
            case "Enterprise":
                course_requirements = "version 0.2\Tracks\Enterprise Computing Track.csv"
                self.populateCourseArray(course_requirements)
            case "Cybersecurity":
                course_requirements = "version 0.2\Tracks\Cybersecurity Track.csv"
                self.populateCourseArray(course_requirements)

    def TrackComboSelected(self, event=None):
        self.trackCallBack(self.trackCombo.get())
        print(self.trackCombo.get())

    def ChatBotCall(self):
        pass

    def Submit(self):
        name = self.nameInput.get()
        path = self.trackCombo.get()
        hours = self.DesiredHours.get()
        print(path)
        self.mainwindow.quit()
        self.mainwindow.destroy()




if __name__ == "__main__":
    root = tk.Tk()
    app = NewprojectApp(root)
    app.trackCombo.current(0)
    app.trackCombo.bind('<<ComboboxSelected>>',app.TrackComboSelected())
    app.trackCombo.bind('<<ComboboxSelected>>',lambda event: app.TrackComboSelected())
    #app.TrackComboSelected()
    app.run()


