import networkx as nx
import fileReader as fr 
from matplotlib import pyplot as plt


fr.populateCourseArray("version 0.2\Tracks\inTest.csv")
fr.getNeededClasses()

#Return Course object by course name
def getCourseObj(courseName):
    foundCourse = None
    for course in fr.courses:
        if course.name == courseName:
            foundCourse = course

    return foundCourse

#Initialize Graph
g = nx.DiGraph()

for course in fr.courses:    
    nodes = course.name

    for i in course.prereq: 
      g.add_edge(i,course.name)


visited2 = []
queue2 = []
path = []

def bfs2(visited, graph, node):
  visited.append(node)
  queue2.append(node)

  while queue2:
    s = queue2.pop(0) 
    #print(s, end = " ")
    path.append(s)

    for neighbour in graph.neighbors(s):
    #for neighbour in g.successors(s):
    #for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue2.append(neighbour)

#connect all nodes with taken prerequistes {"":[CPSC2105,CPSC1302,CPSC2108,MATH5125]}
bfs2(visited2, g, '')
path.remove('')
path2 = []
path3 = []

for p in path:
  if p in fr.notTaken:
    path3.append(getCourseObj(p))
    path2.append(p)

print(path2)
'''
for i in path3:
  if i.spring and i.taken == False:
    print(i.name)
    i.taken = True
    j += i.hours
'''