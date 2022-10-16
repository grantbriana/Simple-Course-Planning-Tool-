import tkinter as tk
import os
from tkinter import filedialog as fd

root = tk.Tk()

#Window creation.
root.title("Simple Course Planning Tool")
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



root.mainloop()

import csv
import PyPDF2

courses = []
notTaken = []

drop = pathMenu.get()

#each class a literal class with attributes course, descript., etc


class course:
    def __init__(self, name, description, hours, fall, spring, summer, prereq, taken):
        # string
        self.name = str(name)
        # string
        self.description = str(description)
        # int
        self.hours = int(hours)
        # bool
        self.fall = True if fall == "TRUE" else False
        # bool
        self.spring = True if spring == "TRUE" else False
        # bool
        self.summer = True if summer == "TRUE" else False
        # dict
        #self.prereq = str(prereq)
        self.prereq = prereq

        # bool
        self.taken = True if taken == "TRUE" else False   #getNeededFunction defines if taken or not

    # Created these functions to grab the information.
    def __str__(
            self):  # ----->This is a string. This will output all the info for a class. ex use / print(course[0])  or print(course[0].Name() for specific info
        return f'{self.name}, {self.description}, {self.hours}, {"Fall"},{self.fall},{"Spring"}, {self.spring}, {"Summer"},{self.summer}, {self.prereq}, {self.taken}'

    def Name(self):
        return self.name

    def Description(self):
        return self.description

    def Hours(self):
        return self.hours

    def Fall(self):
        return self.fall

    def Spring(self):
        return self.spring

    def Summer(self):
        return self.summer

    def Prereq(self):
        return self.prereq

    def Taken(self):
        return self.taken


#stand-in function for student interface module
def getUserTrack(drop):
    match drop:
        #software systems
        case "Software Systems":
            course_requirements = "Q:\SCP tool\Software Systems Track.csv"
            populateCourseArray(course_requirements)
        #education
        case "Game Development":
            course_requirements = "version 0.2\Tracks\Education Track - Sheet1.csv"
            populateCourseArray(course_requirements)
        #cybersecurity
        case "Network Security":
            course_requirements = "version 0.2\Tracks\Cybersecurity Track - Sheet1.csv"
            populateCourseArray(course_requirements)
        #games programming
        case "Game Development":
            course_requirements = "version 0.2\Tracks\Games Programming Track - Sheet1 (1).csv"
            populateCourseArray(course_requirements)
        #web development
        case "Web Development":
            course_requirements = "version 0.2\web development track.csv"
            populateCourseArray(course_requirements)
        #Enterprise
        case "Enterprise":
            course_requirements = "version 0.2\Tracks\Enterprise Computing Track - Sheet1.csv"
            populateCourseArray(course_requirements)


#Creates course classes with proper attributes & appends to courses array for fast retrieval
def populateCourseArray(path):
    #relevant spreadsheet opened
    with open(path, mode='r', encoding='utf-8-sig') as csvfile:
        datareader = csv.reader(csvfile)
        #row[6] (prerequisites) iterated and added to prereq. list

        for row in datareader:
            prereq = row[7].split(",")
            #print(prereq)
            #(self, name, description, hours, fall, spring, summer, prereq, taken):
            newCourse = course(row[0],row[1],row[2],row[3],row[4],row[5],prereq,row[6])
            courses.append(newCourse)

#Keep track of taken classes & needed classes
def getNeededClasses():
    #from gui, retrieve user selected of DegreeWorks File Path
    degreeWorksPath = filePath.get()
    pdfFileObj = open(degreeWorksPath,'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    numPages = PyPDF2.PdfFileReader(pdfFileObj).numPages
    #if course name discovered in user DegreeWorks file, mark as NOT taken
    for i in range(numPages):
        pageObj = pdfReader.getPage(i)
        text=(pageObj.extractText())
        #print(text)
        #parse user's file
        for course in courses:
            if course.name+"*" in text or course.name in text or course.description in text:
                #if course is found in Text, it is not Taken
                notTaken.append(course.name)

    print(notTaken)
getUserTrack(drop)
import networkx as nx
#import fileReader as fr
from matplotlib import pyplot as plt

#populateCourseArray("Q:\SCP tool\Software Systems Track.csv")
#getNeededClasses()


#Return Course object by course name
def getCourseObj(courseName):
    foundCourse = None
    for course in courses:
        if course.name == courseName:
            foundCourse = course

    return foundCourse

#Initialize Graph
g = nx.DiGraph()

for course in courses:
    nodes = course.name

    for i in course.prereq: 
      g.add_edge(i,course.name)


visited2 = []
queue2 = []
path = []

def bfs2(visited, graph, node):
  visited.append(node)
  queue2.append(node)

  while queue2:
    s = queue2.pop(0) 
    #print(s, end = " ")
    path.append(s)

    for neighbour in graph.neighbors(s):
    #for neighbour in g.successors(s):
    #for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue2.append(neighbour)

#connect all nodes with taken prerequistes {"":[CPSC2105,CPSC1302,CPSC2108,MATH5125]}
bfs2(visited2, g, '')
path.remove('')
path2 = []
path3 = []

for p in path:
  if p in p.notTaken:
    path3.append(getCourseObj(p))
    path2.append(p)

print(path2)
'''
for i in path3:
  if i.spring and i.taken == False:
    print(i.name)
    i.taken = True
    j += i.hours
'''