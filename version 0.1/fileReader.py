# import student interface module & needed packages
import csv
import PyPDF2
import GUI as gui

courses = []

drop = gui.pathMenu.get()

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
        self.prereq = str(prereq)
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
            course_requirements = "version 0.1\Tracks\Software Systems Track.csv"
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
def populateCourseArray(path):
    #relevant spreadsheet opened
    with open(path, 'r') as csvfile:
        datareader = csv.reader(csvfile)

        #row[6] (prerequisites) iterated and added to prereq. list
        prereq = [] 

        for row in datareader:
            newCourse = course(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7])
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