import csv
import pathlib
import tkinter.messagebox

import pygubu
import tkinter as tk
import webbrowser
import os
from tkinter import filedialog as fd
PROJECT_PATH = pathlib.Path(__file__).parent

PROJECT_UI =  "SCPToolUi2.ui"
pathLine = ""

class NewprojectApp:


    def __init__(self, master=None):
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        # Main widget
        self.mainwindow = builder.get_object("frame1", master)
        builder.connect_callbacks(self)
        self.trackCombo = tk.combobox = builder.get_object('TrackCombo')
        self.nameInput = tk.entry = builder.get_object('nameInput')
        self.nameInput.insert(0,'Enter Your Name')
        self.ClassList = builder.get_object('CourseList')
        self.DesiredHours = builder.get_object('entry2')
        self.DesiredHours.insert(0, "12")
        options = ("Software Systems", "Game Development", "Cybersecurity", "Education", "Web Development", "Enterprise")
        self.trackCombo.config(values=options)
        self.trackCombo['state'] = 'readonly'
        self.trackCombo.current(0)

        self.DegreeWork = tk.StringVar()

    def populateCourseArray(self, path):
        # relevant spreadsheet opened
        i = 0
        with open(path, 'r') as csvfile:
            datareader = csv.reader(csvfile)
            # row[6] (prerequisites) iterated and added to prereq. list
            self.ClassList.delete(0,tk.END)
            for row in datareader:
                #prereq = row[7].split(",")
                self.ClassList.insert(i, row[1])
                i = i + 1


    def trackCallBack(self, drop):
        match drop:
            # software systems
            case "Software Systems":
                course_requirements = "version 0.2\Tracks\Software Systems Track.csv"
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

    def callback(self, event=None):
        filename = 'file://'+os.getcwd()+'/'+'webChat.html'
        print(filename)
        webbrowser.open_new_tab(filename)

    def Track(self):
        return self.trackCombo.get()


    def run(self):
        self.mainwindow.mainloop()

    def degreeWorksPath(self):
        filePath = tk.StringVar()
        filename = fd.askopenfilename()
        filePath.set(filename)
        self.DegreeWork.set(filename)
    def DegreeWork(self):
        return self.DegreeWork

    def ChatBotCall(self):
        pass

    def Submit(self):
        path= self.trackCombo.get()
        if not self.DegreeWork.get():
            res = tkinter.messagebox.askquestion(title='Degree Works File Not Found', message='You do not have a Degree Works selected. Do you wish to continue without a Degree Works file?')
            if res == 'yes':
                self.mainwindow.quit()
        else:
            self.mainwindow.quit()






root = tk.Tk()
app = NewprojectApp(root)
app.trackCombo.bind("<<ComboboxSelected>>", app.trackCallBack(app.trackCombo.get()))
app.trackCombo.bind("<<ComboboxSelected>>", lambda event:app.trackCallBack(app.trackCombo.get()))
app.run()
filePath = tk.StringVar
#ilePath.set(app.DegreeWork().get)
