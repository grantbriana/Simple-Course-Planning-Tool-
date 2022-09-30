# import student interface module & needed packages
import csv
import PyPDF2
import gui

courses = []

#drop = gui.drop
drop = gui.pathMenu.get()

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
def getUserTrack(drop):
    match drop:
        #software systems
        case "Software Systems":
            course_requirements = "Tracks/Software Systems Track - Sheet1 (1).csv"
            populateCourseArray(course_requirements)
        #education
        case "Game Development":
            course_requirements = "Tracks/Education Track - Sheet1.csv"
            populateCourseArray(course_requirements)
        #cybersecurity
        case "Network Security":
            course_requirements = "Tracks/Cybersecurity Track - Sheet1.csv"
            populateCourseArray(course_requirements)
        #games programming
        case "Game Development":
            course_requirements = "Tracks/Games Programming Track - Sheet1 (1).csv"
            populateCourseArray(course_requirements)
        #web development
        case "Web Development":
            course_requirements = "web development track.csv"
            populateCourseArray(course_requirements)
        #Enterprise
        case "Enterprise":
            course_requirements = "Tracks/Enterprise Computing Track - Sheet1.csv"
            populateCourseArray(course_requirements)

#Creates course classes with proper attributes & appends to courses array for fast retrieval
def populateCourseArray(track):
    #relevant spreadsheet opened
    with open(track, 'r') as csvfile:
        datareader = csv.reader(csvfile)

        #row[6] (prerequisites) iterated and added to prereq. list
        prereq = [] 

        for row in datareader:
            newCourse = course(row[0],row[1],row[2],row[3],row[4],row[5],row[6])
            courses.append(newCourse)


#Keep track of taken classes & needed classes
def getNeededClasses():
    #from gui, retrieve user selected of DegreeWorks File Path 
    degreeWorksPath = gui.filePath.get()
    pdfFileObj = open(degreeWorksPath,'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    numPages = PyPDF2.PdfFileReader(pdfFileObj).numPages
    #if course name discovered in user DegreeWorks file, mark as NOT taken
    for i in range(numPages):
        pageObj = pdfReader.getPage(i)
        text=(pageObj.extractText())
        
        #parse user's file
        for course in courses:
            if course.name in text:
                course.taken = False

getUserTrack(drop)
getNeededClasses()