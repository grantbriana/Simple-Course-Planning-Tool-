#Initializes Breadth-First Graph Traversal
import networkx as nx
import fileReader as fr

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
  # if p in fr.notTaken:
  objpath.append(getCourseObj(p))
  if getCourseObj(p).taken == False:
    unTakenPath.append(p)
    print(getCourseObj(p))


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