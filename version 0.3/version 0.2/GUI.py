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
        self.pathMenu = None
        builder.import_variables(self, ['pathMenu'])
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
        self.pathMenu = self.trackCombo.get()
        pathMenu = self.pathMenu
        hours = self.DesiredHours.get()
        print(self.pathMenu)
        self.mainwindow.quit()
        self.mainwindow.destroy()
    def PathMenu(self):
        return self.pathMenu.get()

root = tk.Tk()
app = NewprojectApp(root)
app.trackCombo.current(0)
app.trackCombo.bind('<<ComboboxSelected>>',app.TrackComboSelected())
app.trackCombo.bind('<<ComboboxSelected>>',lambda event: app.TrackComboSelected())
#app.TrackComboSelected()
app.run()
pathMenu = tk.StringVar()
pathMenu = app.pathMenu


