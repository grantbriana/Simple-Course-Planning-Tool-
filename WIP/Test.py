#!/usr/bin/env python
# coding: utf-8

# In[55]:


import pandas
import csv
from pathlib import Path
import networkx as nx
from matplotlib import pyplot as plt

path = Path("Documents\Software Systems Track.csv")
courses = []


class course:
    def __init__(self, name, description, hours, fall, spring, summer, prereq, taken):
        # string
        self.name = name
        # string
        self.description = description
        # int
        self.hours = int(hours)
        # bool
        self.fall = True if fall == "TRUE" else False
        # bool
        self.spring = True if spring == "TRUE" else False
        # bool
        self.summer = True if summer == "TRUE" else False
        # dict
        self.prereq = prereq
        # bool
        self.taken = True if taken == "TRUE" else False

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


def populateCourseArray(path):
    with open(path, 'r', encoding='utf-8') as csvfile:
        datareader = csv.reader(csvfile)
        for row in datareader:
            newCourse = course(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            courses.append(newCourse)



populateCourseArray(path)

print(len(courses))


#-------------------------Schedule Constructor____________________________
tempArray = []
courseArray = []
classesArrayStage = []
Working = True

for i in courses:
    classesArrayStage.append(i)

def prereqCheck(course):
    if(course.taken == False):
        if not tempArray:
            return False
            print("empty")
        else:            
            for i in tempArray:
                if i.name == course.prereq:
                    return True                           
                else:
                    return False
    else:
        print("Whoops")
        return True
def scheduleCreate():
    while Working:
        tempArray = []
        j = 0
        for course in courses:
            if(j <= 12):
                if prereqCheck(course) == False:
                    tempArray.append(course)
                    j = j + course.hours
                    course.taken = True
        if(not tempArray):
            break
        courseArray.append(tempArray)  
#calls the function
scheduleCreate()

#out the classes. For testing purposes
k = 0
for course in courseArray:
    print("\n" + "Semester: " + str(k) + "\n")
    k = k + 1
    for i in course:
        print(i)
# print("\n\nSecond Semester - Summer \n")
# for clasess in semesterTwo:
#     print(clasess)
# print("\n\nThrid Semester - Fall \n")
# for clasess in semesterThree:
#     print(clasess)
# print("\n\nFourth Semester - Spring \n")
# for clasess in semesterFour:
#     print(clasess)
# print("\n\nFifth Semester - Summer \n")
# for clasess in semesterFive:
#     print(clasess)
# print("\n\nSixth Semester - Fall \n")
# for clasess in semesterSix:
#     print(clasess)
# print("\n\nSeventh Semester - Spring \n")
# for clasess in semesterSeven:
#     print(clasess)
# print("\n\nEighth Semester - Summer \n")
# for clasess in semesterEight:
#     print(clasess)          


# group nodes by column
left_nodes = []
middle_nodes = []
right_nodes = []

graph = nx.DiGraph()
graph.add_node("Senior")
graph.add_node("Senior/Junior")

for course in courses:
    graph.add_node(course.name)
j = 0    
for classes in courses:
    for classes2 in courses:
        if classes2.prereq == classes.name:
            graph.add_edge(classes.name, classes2.name)
        elif classes.prereq == "Senior":
            graph.add_edge(classes.name, "Senior")
        elif classes.prereq == "Senior/Junior":
            graph.add_edge(classes.name, "Senior")
            graph.add_edge(classes.name, "Senior/Junior")
for classes in courses:
    if graph.nodes(classes):
        graph.add_node(classes.name)


for classes in courses:
    if classes.prereq == "":
        left_nodes.append(classes.name)
    else:
        for classes2 in courses:
            if classes.prereq != "" and classes.name == classes2.prereq:
                middle_nodes.append(classes.name)
            elif classes.prereq != "" and classes.name != classes2.prereq:
                right_nodes.append(classes)

# pos = nx.DiGraph({n: (0, i) for i, n in enumerate(left_nodes)})
# pos.update({n: (1, i + 0.5) for i, n in enumerate(middle_nodes)})
# pos.update({n: (2, i + 0.5) for i, n in enumerate(right_nodes)})

plt.figure(1,figsize=(12,12))
print(len(graph.nodes()))
d = dict(graph.degree)
list(nx.topological_sort(graph))
plt.tight_layout()
nx.draw(graph, with_labels=True,font_weight='bold', node_size=500)
ax = plt.gca()
ax.margins(0.01)
plt.axis("off")
plt.show()
i = 0;
list(reversed(list(nx.topological_sort(graph))))
graph.edges()


# In[ ]:





# In[ ]:




