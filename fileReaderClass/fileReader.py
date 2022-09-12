# import student interface module & needed packages
#1from sqlite3.dbapi2 import _SingleParamWindowAggregateClass
import pandas
import csv

# Based on user track inputted, select relevant track courses
path = "software systems.csv"
track = input("Enter track")
courses = []

#each class a literal class with attributes course, descript., etc
class course:
    def __init__(self,name, description, hours, fall, spring, summer):
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
        #self.prereq = prereq

def getNeededClasses():
    match track:
        #enterprise computing
        case 1:
            df = pandas.read_csv(path)
        #education
        case 2:
            df = pandas.read_csv(path)
        #software systems
        case 3:
            df = pandas.read_csv("software systems.csv")
            track2 = "software systems.csv"
        #cybersecurity
        case 4:
            df = pandas.read_csv(path)
        #games programming
        case 5:
            df = pandas.read_csv(path)
        #web development
        case 6:
            df = pandas.read_csv(path)

#Creates course classes with proper attributes & appends to courses array for fast retrieval
def populateCourseArray():
    with open("software systems.csv", 'r') as csvfile:
        datareader = csv.reader(csvfile)
        prereq = [] 
        for row in datareader:
            newCourse = course(row[0],row[1],row[2],row[3],row[4],row[5])
            courses.append(newCourse)