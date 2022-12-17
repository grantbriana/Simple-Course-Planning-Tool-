# import student interface module & needed packages
import csv
import os
import PyPDF2
import json
courses = []
notTaken = []

def readJsonFile():
   fileName = ""
   with open('upload.json', 'r') as openfile:
      # Reading from json file
      jsonFile = json.load(openfile)
      fileName = "uploads/" + jsonFile["fileName"]
      #print(fileName)
   return fileName

def readJsonTrack():
   track = ""
   with open('upload.json', 'r') as openfile:
      # Reading from json file
      jsonFile = json.load(openfile)
      track = jsonFile["track"]
      #print(track)
   return track

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
def getUserTrack():
    drop = readJsonTrack()
    match drop:
        #software systems
        case "Software Systems":
            course_requirements = "Tracks\Software Systems Track.csv"
            populateCourseArray(course_requirements)
        #education
        case "Education":
            course_requirements = "Tracks\Education Track.csv"
            populateCourseArray(course_requirements)
        #cybersecurity
        case "Network Security":
            course_requirements = "Tracks\Cybersecurity Track.csv"
            populateCourseArray(course_requirements)
        #games programming
        case "Game Development":
            course_requirements = "Tracks\Games Programming Track.csv"
            populateCourseArray(course_requirements)
        #web development
        case "Web Development":
            course_requirements = "Tracks\web development track.csv"
            populateCourseArray(course_requirements)
        #Enterprise
        case "Enterprise":
            course_requirements = "Tracks\Enterprise Computing Track.csv"
            populateCourseArray(course_requirements)
        case "Cybersecurity":
            course_requirements = "Tracks\Cybersecurity Track.csv"
            populateCourseArray(course_requirements)


#Creates course classes with proper attributes & appends to courses array for fast retrieval
def populateCourseArray(path):
    #relevant spreadsheet opened
    with open(path, 'r') as csvfile:
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
    #from dropdown, retrieve user selected of DegreeWorks File Path
    degreeWorksPath = readJsonFile()

    pdfFileObj = open(degreeWorksPath,'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    numPages = PyPDF2.PdfFileReader(pdfFileObj).numPages
        #if course name discovered in user DegreeWorks file, mark as NOT taken
    for i in range(numPages):
        pageObj = pdfReader.getPage(i)
        text=(pageObj.extractText())
            #parse user's file
        for course in courses:
            if course.name+"*" in text or course.name in text:
                    #if course is found in Text, add to untaken list
                notTaken.append(course.name)
        #print("\n")
        #if course name NOT discovered in user untaken list, mark as taken
    for c in courses:
        if c.name not in notTaken:
            c.taken = True

getUserTrack()
getNeededClasses()
