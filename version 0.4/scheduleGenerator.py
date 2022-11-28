import fileReader as fr
import GUI2 as gui

tempArray = []
courseArray = []
classesArrayStage = []
Working = True
desiredHours = int(gui.app.DesiredHours.get())
for i in fr.courses:
    classesArrayStage.append(i)

#checks if courses prereq has been taken
def prereqCheck(course):
    #indicates no course prerequisite
    if course.prereq != "":
        istaken = False
        #iterate thorugh courses list
        for course2 in fr.courses:
            #if the course prerequisite is in the list and taken
            if (course.prereq == course2.name) and course2.taken == True:
                istaken = True
        return istaken
    else:
        return False
   
        
#builds each semester based on if it is during the
def scheduleCreate():
    while Working:
        tempArray = []
        j = 0
        for course in fr.courses:
            if(j < desiredHours):
                if course.spring == True:
                    if (course.taken == False):
                        if tempArray:
                            isAPrereq = False
                            for i in tempArray:
                                if i.name == course.prereq:
                                    isAPrereq = True
                                else:
                                    isAPrereq = False
                            if ((isAPrereq == False and prereqCheck(course) == True) or course.prereq ==""):
                                tempArray.append(course)
                                j = j + course.hours
                        elif not tempArray:
                            tempArray.append(course)
                            j = j + course.hours

                #else:

        if(not tempArray):
            break
        courseArray.append(tempArray)
        for i in tempArray:
            i.taken = True

        tempArray = []
        j = 0
        for course in fr.courses:
            if(j < desiredHours):
                if course.summer == True:
                    if (course.taken == False):
                        if tempArray:
                            isAPrereq = False
                            for i in tempArray:
                                if i.name == course.prereq:
                                    isAPrereq = True
                                else:
                                    isAPrereq = False
                            if ((isAPrereq == False and prereqCheck(course) == True) or course.prereq ==""):
                                tempArray.append(course)
                                j = j + course.hours
                        elif not tempArray:
                            tempArray.append(course)
                            j = j + course.hours

                #else:

        if(not tempArray):
            break
        courseArray.append(tempArray)
        for i in tempArray:
            i.taken = True

        tempArray = []
        j = 0
        for course in fr.courses:
            if(j < desiredHours):
                if course.fall == True:
                    if (course.taken == False):
                        if tempArray:
                            isAPrereq = False
                            for i in tempArray:
                                if i.name == course.prereq:
                                    isAPrereq = True
                                else:
                                    isAPrereq = False
                            if ((isAPrereq == False and prereqCheck(course) == True) or course.prereq ==""):
                                tempArray.append(course)
                                j = j + course.hours
                        elif not tempArray:
                            tempArray.append(course)
                            j = j + course.hours

                #else:

        if(not tempArray):
            break
        courseArray.append(tempArray)
        for i in tempArray:
            i.taken = True


#out the classes. For testing purposes
k = 1
def season():
    if k in (1, 4, 7, 10):
        return "Spring"
    elif k in (2, 5, 8, 11):
        return  "Summer"
    elif k in (3, 6, 9, 12):
        return  "Fall"



# Demo
fr.getUserTrack(fr.drop)
fr.getNeededClasses()
#calls the function
scheduleCreate()

f = open("demofile.txt", "w")
for course in courseArray:
    print("\n" + "Semester: " + str(k) + " " + season() + "\n")
    f.write("\n" + "Semester: " + str(k) + " " + season() + "\n")

    k = k + 1
    for i in course:
        print(i)
        f.write(str(i) + "\n")
f.close()

# https://github.com/grantbriana/Simple-Course-Planning-Tool-