# import student interface module & needed packages
#1from sqlite3.dbapi2 import _SingleParamWindowAggregateClass
import pandas
import csv

# Based on user track inputted, select relevant track courses
path = ""
studentName = input("Please enter your name.\n")

courses = []

#each class a literal class with attributes course, descript., etc
class course:
    def __init__(self,name, description, hours, fall, spring, summer, prereq, taken):
        #string
        self.name = name
        #string
        self.description = description
        #int
        self.hours = hours
        #bool
        self.fall = fall
        #bool
        self.spring = spring
        #bool
        self.summer = summer
        #dict
        self.prereq = prereq
        #bool
        self.taken = taken

#Created these functions to grab the information.
    def __str__(self): #----->This is a string. This will output all the info for a class. ex use / print(course[0])  or print(course[0].Name() for specific info
        return f'{self.name}, {self.description}, {self.hours}, {self.fall}, {self.spring}, {self.summer}, {self.prereq}, {self.taken}'
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

#Creates course classes with proper attributes & appends to courses array for fast retrieval
def populateCourseArray(path):
    with open(path, 'r', encoding='utf-8') as csvfile:
        datareader = csv.reader(csvfile)
        #prereq = []
        for row in datareader:
            newCourse = course(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            courses.append(newCourse)

def getNeededClasses(track):
    match track:
        #enterprise computing
        case 1:
            #df = pandas.read_csv(path)
            print("no schedule available.")
        #education3
        case 2:
            #df = pandas.read_csv(path)
            print("no schedule available.")
        #software systems
        case 3:
            #df = pandas.read_csv("Q:\SCP tool\Software Systems Track.csv")
            #track = "Q:\SCP tool\Software Systems Track.csv"
            path = "Q:\SCP tool\Software Systems Track.csv"
            populateCourseArray(path)
        #cybersecurity
        case 4:
            #df = pandas.read_csv(path)
            print("no schedule available.")
        #games programming
        case 5:
            #df = pandas.read_csv(path)
            print("no schedule available.")
        #web development
        case 6:
            #df = pandas.read_csv(path)
            
            print("no schedule available.")
getNeededClasses(int(input("Enter track \n Options \n3 - Software Systems \n")))
#-------------------------Schedule Constructor____________________________

#semester and student info array's
studentInfo = []
semesterOne = []
semesterTwo = []
semesterThree = []
semesterFour = []
semesterFive = []
semesterSix = []
semesterSeven = []
semesterEight = []
classesArrayStage = []

#This function goes through the list of classes and checks if the class hours is greater then 12, if the class has been taken before, and for the season that the semester is being taken in
def scheduleCreate():
    i = 0
    for classes in courses:
        if(i <= 12):
            if(classes.taken != True):
                if(classes.Spring() != False):
                    if(prereqCheck(classes) != False):
                        semesterOne.append(classes)
                        i += int(classes.Hours())
                        classes.taken = True
    i = 0
    for classes in courses:
        if(i <= 12):
            if(classes.taken != True):
                if (classes.Summer() != False):
                    if (prereqCheck(classes) != False):
                        semesterTwo.append(classes)
                        i += int(classes.Hours())
                        classes.taken = True
    i = 0
    for classes in courses:
        if(i <= 12):
            if(classes.taken != True):
                if (classes.Fall() != False):
                    if (prereqCheck(classes) != False):
                        semesterThree.append(classes)
                        i += int(classes.Hours())
                        classes.taken = True
    i = 0
    for classes in courses:
        if(i <= 12):
            if(classes.taken != True):
                if (classes.Spring() != False):
                    if (prereqCheck(classes) != False):
                        semesterFour.append(classes)
                        i += int(classes.Hours())
                        classes.taken = True
    i = 0
    for classes in courses:
        if(i <= 12):
            if(classes.taken != True):
                if (classes.Summer() != False):
                    if (prereqCheck(classes) != False):
                        semesterFive.append(classes)
                        i += int(classes.Hours())
                        classes.taken = True
    i = 0
    for classes in courses:
        if(i <= 12):
            if(classes.taken != True):
                if (classes.Fall() != False):
                    if (prereqCheck(classes) != False):
                        semesterSix.append(classes)
                        i += int(classes.Hours())
                        classes.taken = True
    i = 0
    for classes in courses:
        if(i <= 12):
            if(classes.taken != True):
                if (classes.Spring() != False):
                    if (prereqCheck(classes) != False):
                        semesterSeven.append(classes)
                        i += int(classes.Hours())
                        classes.taken = True
    i = 0
    for classes in courses:
        if(i <= 12):
            if(classes.taken != True):
                if (classes.Summer() != False):
                    if (prereqCheck(classes) != False):
                        semesterEight.append(classes)
                        i += int(classes.Hours())
                        classes.taken = True
def prereqCheck(course):
    if(course.prereq != ""):
        for classes in courses:
            if (course.prereq != classes.Name() and classes.taken != True):
                return False
            else:
                return True
    else:
        return True

#calls the function
scheduleCreate()

#out the classes. For testing purposes
print("\n\nFirst Semester \n")
for clasess in semesterOne:
    print(clasess)
print("\n\nSecond Semester \n")
for clasess in semesterTwo:
    print(clasess)
print("\n\nThrid Semester \n")
for clasess in semesterThree:
    print(clasess)
print("\n\nFourth Semester \n")
for clasess in semesterFour:
    print(clasess)
print("\n\nFifth Semester \n")
for clasess in semesterFive:
    print(clasess)
print("\n\nSixth Semester \n")
for clasess in semesterSix:
    print(clasess)
print("\n\nSeventh Semester \n")
for clasess in semesterSeven:
    print(clasess)
print("\n\nEighth Semester \n")
for clasess in semesterEight:
    print(clasess)
