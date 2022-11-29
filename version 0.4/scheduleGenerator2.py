#Generates Schedule. Imports BFS graph
import DAG2 as dag
import GUI2 as gui

desiredHours = int(gui.app.DesiredHours.get())
print(desiredHours)

#Checks if class in temporary array to avoid unmet prerequisite error
def notListed(course,array):
  flag = False
  courseObj = dag.getCourseObj(course)
  if courseObj.prereq != [""]:
    for i in courseObj.prereq:
      if i in array:
        flag = True
  return flag

#CourseArray to hold all Semesters
courseArray = []
def schedule():
  totalClasses = len(dag.unTakenPath)
  #Loop runs on condition that all classes have not been added to a semester (array)
  while totalClasses != 0:
    tempArray = []
    #semester hours counter.
    j = 0


    #Iterate through each class in BFS (level-traversal)path
    for course in dag.objpath:
      # Check if 15 array does not exceed 15 credit hours
      if j < desiredHours:
      #Check if  is available for season
        if course.fall:
          #check if class has been taken and not already in semester array
          if course.taken == False:
            if course not in tempArray:
              #check if course has prereqs or course has met all prereqs
              if dag.prereqCheck(course.name):
                #check if course has a prerequisite in semester array already
                if notListed(course.name,tempArray) == False:
                  tempArray.append(course.name)
                  course.taken = True
                  j += course.hours
                  totalClasses -= 1
    courseArray.append(tempArray)
    if(totalClasses == 0):
      break

    #Repeat for next semester
    tempArray = []
    j = 0
    for course in dag.objpath:
      if j < desiredHours:
        if course.summer:
          if course.taken == False:
            if course not in tempArray:  
              if dag.prereqCheck(course.name):
                if notListed(course.name,tempArray) == False:
                  tempArray.append(course.name)
                  course.taken = True
                  j += course.hours
                  totalClasses -= 1
    courseArray.append(tempArray)
    
    if(totalClasses == 0):
      break
    

    #Repeat for nest semester
    tempArray = []
    j = 0
    for course in dag.objpath:
      if j < desiredHours:
        if course.spring:
          if course.taken == False:
            if course not in tempArray:  
              if dag.prereqCheck(course.name):
                if notListed(course.name,tempArray) == False:
                  tempArray.append(course.name)
                  course.taken = True
                  j += course.hours
                  totalClasses -= 1
    courseArray.append(tempArray)
    
    if(totalClasses == 0):
      break
    noCLasses = False

schedule()


k = 1
def season():
    if k == 1 or (k % 3 == 1):
        return "Spring"
    elif k == 2 or (k % 3 == 2):
        return  "Summer"
    elif k == 3 or (k % 3 == 0):
        return  "Fall"

