# import student interface module & needed packages
from pickle import TRUE
import csv
import PyPDF2

# Based on user track inputted, select relevant track courses
path = "software systems.csv"
courses = []

#each class a literal class with attributes course, descript., etc
class course:
    def __init__(self,name, description, hours, fall, spring, summer,taken):
        #string
        self.name = name
        #string]
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
        self.taken = taken


#stand-in function for student interface module
def getNeededClasses():
    track = input("Enter track")
    match track:
        #enterprise computing
        case 1:
            track = "enterprise computing track.csv"
            #populateCourseArray(track)
        #education
        case 2:
            track = "education track.csv"
            #populateCourseArray(track)
        #software systems
        case 3:
            populateCourseArray()
        #cybersecurity
        case 4:
            track = "cybersecurity track.csv"
            #populateCourseArray(track)
            #df = pandas.read_csv(path)
        #games programming
        case 5:
            track = "games programming track.csv"
            #populateCourseArray()
        #web development
        case 6:
            track = "web development track.csv"
            #populateCourseArray()

#Creates course classes with proper attributes & appends to courses array for fast retrieval
def populateCourseArray():
    #relevant spreadsheet opened
    with open("software systems track2.csv", 'r') as csvfile:
        datareader = csv.reader(csvfile)

        prereq = [] 

        for row in datareader:
            newCourse = course(row[0],row[1],row[2],row[3],row[4],row[5],row[6])
            courses.append(newCourse)

populateCourseArray()


#Keep track of taken classes & needed classes
def getNeededClasses2():
    pdfFileObj = open('Sample Input3.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    pageObj = pdfReader.getPage(2)
    text=(pageObj.extractText())

    #parse user's file
    for course in courses:
        if course.description in text:
            print(course.name)
            course.taken = False

getNeededClasses()
getNeededClasses2()