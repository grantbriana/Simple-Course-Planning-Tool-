import networkx as nx
import fileReader as fr 
from matplotlib import pyplot as plt

#Initialize Graph
g = nx.DiGraph()
#Breadth-First Graph Traversal: Explores graph level by level
visited = []
queue = []
path = []

for course in fr.courses:    
  #Create graph edges for adjacency list
  for i in course.prereq: 
    g.add_edge(i,course.name)


#Return Course object by course name
def getCourseObj(courseName):
  foundCourse = None
  for course in fr.courses:
    if course.name == courseName:
      foundCourse = course

  return foundCourse


level = {} #dict {level: node}

for c in fr.courses:
  level[c.name] = -1
level[''] = -1


def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)
  level[node] = 0

  while queue:
    s = queue.pop(0) 
    path.append(s)

    for neighbour in graph.neighbors(s):
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)
        level[neighbour] = level[s] + 1

    
bfs(visited, g, '')
path.remove('')
unTakenPath = []
objpath = []

for p in path:
  if p in fr.notTaken:
    objpath.append(getCourseObj(p))
    unTakenPath.append(p)


# ---- For testing purposes and schedule generation ----

#Tests if course has met prereqs
def prereqCheck(course):
  courseObj = getCourseObj(course)
  if(courseObj.prereq != [""]):
    for i in courseObj.prereq:
      prereqObj = getCourseObj(i)
      #find i course object. check if object is taken
      if(prereqObj.taken == False):
        return False
  return True

#Tests BFS
def lessThan(course):
  flag = False
  courseObj = getCourseObj(course)
  if(courseObj.prereq != [""]):
    #iterate through course prereqs
    for i in courseObj.prereq:   
      if i in unTakenPath:
        #if prereq after course
        if unTakenPath.index(i) > unTakenPath.index(course):
          flag = True
  return flag


#Checks if class in temporary array to avoid unmet prerequisite error
def notListed(course,array):
  flag = False
  courseObj = getCourseObj(course)
  if courseObj.prereq != [""]:
    for i in courseObj.prereq:
      if i in array:
        flag = True
  return flag

#CourseAray to hold all Semesters
courseArray = []
def schedule():
  totalClasses = len(unTakenPath)
  #Loop runs on condition that all classes have not been added to a semester (array)
  while totalClasses != 0:
    tempArray = []
    #semester hours counter. 
    j = 0
    #Check if 15 array does not exceed 15 credit hours
    if j < 15:
      #Iterate through each class in BFS (level-traversal)path
      for course in objpath:
        #Check if class is available for season
        if course.fall:
          #check if class has been taken and not already in semester array
          if course.taken == False:
            if course not in tempArray: 
              #check if course has prereqs or course has met all prereqs 
              if prereqCheck(course.name):
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
    for course in objpath:
      if j < 15:
        if course.spring:
          if course.taken == False:
            if course not in tempArray:  
              if prereqCheck(course.name):
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
    for course in objpath:
      if j < 15:
        if course.summer:
          if course.taken == False:
            if course not in tempArray:  
              if prereqCheck(course.name):
                if notListed(course.name,tempArray) == False:
                  tempArray.append(course.name)
                  course.taken = True
                  j += course.hours
                  totalClasses -= 1
    courseArray.append(tempArray)
    if(totalClasses == 0):
      break


schedule()
for i in courseArray:
  print(i)

k = 1
def season():
    if k in (1, 4, 7):
        return "Spring"
    elif k in (2, 5, 8):
        return  "Fall"
    elif k in (3, 6, 9):
        return  "Summer"

for course in courseArray:
  print("\n" + "Semester: " + str(k) + " " + season() + "\n")
  k += 1
  for i in course:
    courseObj = getCourseObj(i)
    print(i,":",courseObj.description," Credit Hours: ",courseObj.hours)