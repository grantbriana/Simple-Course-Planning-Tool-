#!/usr/bin/env python
# coding: utf-8

# In[71]:


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
        self.hours = hours
        # bool
        self.fall = bool(fall)
        # bool
        self.spring = bool(spring)
        # bool
        self.summer = bool(summer)
        # dict
        self.prereq = prereq
        # bool
        self.taken = taken

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
semesterOne = []
semesterTwo = []
semesterThree = []
semesterFour = []
semesterFive = []
semesterSix = []
semesterSeven = []
semesterEight = []
classesArrayStage = []

for i in courses:
    classesArrayStage.append(i)

def scheduleCreate():
    j = 0
    prereq = False
    for classes in courses:
        if(j <= 12):
            if(classes.taken != True):
                if(classes.spring == True):
                    if(prereqCheck(classes) != False):
                        for i in semesterOne:
                            if i.name == classes.prereq:
                                prereq = True                           
                            else:
                                prereq = False
                        if prereq == False:
                            semesterOne.append(classes)
                            j = j + int(classes.hours)
                            classes.taken = True
    j = 0
    prereq = False
    for classes in courses:
        if(j <= 12):
            if(classes.taken != True):
                if(classes.summer == True):
                    if(prereqCheck(classes) != False):
                        for i in semesterTwo:
                            if i.name == classes.prereq:
                                prereq = True                           
                            else:
                                prereq = False
                        if prereq == False:
                            semesterTwo.append(classes)
                            j = j + int(classes.hours)
                            classes.taken = True
    j = 0
    prereq = False
    for classes in courses:
        if(j <= 12):
            if(classes.taken != True):
                if(classes.fall != False):
                    if(prereqCheck(classes) != False):
                        for i in semesterThree:
                            if i.name == classes.prereq:
                                prereq = True                           
                            else:
                                prereq = False
                        if prereq == False:
                            semesterThree.append(classes)
                            j = j + int(classes.hours)
                            classes.taken = True
    j = 0
    prereq = False
    for classes in courses:
        if(j <= 12):
            if(classes.taken != True):
                if(classes.spring != False):
                    if(prereqCheck(classes) != False):
                        for i in semesterFour:
                            if i.name == classes.prereq:
                                prereq = True                           
                            else:
                                prereq = False
                        if prereq == False:
                            semesterTwo.append(classes)
                            j = j + int(classes.hours)
                            classes.taken = True
    j = 0
    prereq = False
    for classes in courses:
        if(j <= 12):
            if(classes.taken != True):
                if(classes.summer != False):
                    if(prereqCheck(classes) != False):
                        for i in semesterFive:
                            if i.name == classes.prereq:
                                prereq = True                           
                            else:
                                prereq = False
                        if prereq == False:
                            semesterFive.append(classes)
                            j = j + int(classes.hours)
                            classes.taken = True
                            
    j = 0
    prereq = False
    for classes in courses:
        if(j <= 12):
            if(classes.taken != True):
                if(classes.fall != False):
                    if(prereqCheck(classes) != False):
                        for i in semesterSix:
                            if i.name == classes.prereq:
                                prereq = True                           
                            else:
                                prereq = False
                        if prereq == False:
                            semesterSix.append(classes)
                            j = j + int(classes.hours)
                            classes.taken = True
    j = 0
    prereq = False
    for classes in courses:
        if(j <= 12):
            if(classes.taken != True):
                if(classes.spring != False):
                    if(prereqCheck(classes) != False):
                        for i in semesterSeven:
                            if i.name == classes.prereq:
                                prereq = True                           
                            else:
                                prereq = False
                        if prereq == False:
                            semesterSeven.append(classes)
                            j = j + int(classes.hours)
                            classes.taken = True
    j = 0
    prereq = False
    for classes in courses:
        if(j <= 12):
            if(classes.taken != True):
                if(classes.summer != False):
                    if(prereqCheck(classes) != False):
                        for i in semesterEight:
                            if i.name == classes.prereq:
                                prereq = True                           
                            else:
                                prereq = False
                        if prereq == False:
                            semesterEight.append(classes)
                            j = j + int(classes.hours)
                            classes.taken = True
def prereqCheck(course):
    if(course.prereq != ""):
        for classes in courses:
            if (course.prereq != classes.Name() and classes.taken != True):
                return False
            else:
                return True
    else:
        return True

#calls the function
scheduleCreate()

#out the classes. For testing purposes
print("\n\nFirst Semester - Spring \n")
for clasess in semesterOne:
    print(clasess)
print("\n\nSecond Semester - Summer \n")
for clasess in semesterTwo:
    print(clasess)
print("\n\nThrid Semester - Fall \n")
for clasess in semesterThree:
    print(clasess)
print("\n\nFourth Semester - Spring \n")
for clasess in semesterFour:
    print(clasess)
print("\n\nFifth Semester - Summer \n")
for clasess in semesterFive:
    print(clasess)
print("\n\nSixth Semester - Fall \n")
for clasess in semesterSix:
    print(clasess)
print("\n\nSeventh Semester - Spring \n")
for clasess in semesterSeven:
    print(clasess)
print("\n\nEighth Semester - Summer \n")
for clasess in semesterEight:
    print(clasess)          


# group nodes by column
# left_nodes = []
# middle_nodes = []
# right_nodes = []

# graph = nx.DiGraph()
# graph.add_node("Senior")
# graph.add_node("Senior/Junior")

# for course in courses:
#     graph.add_node(course.name)
# j = 0    
# for classes in courses:
#     for classes2 in courses:
#         if classes2.prereq == classes.name:
#             graph.add_edge(classes.name, classes2.name)
#         elif classes.prereq == "Senior":
#             graph.add_edge(classes.name, "Senior")
#         elif classes.prereq == "Senior/Junior":
#             graph.add_edge(classes.name, "Senior")
#             graph.add_edge(classes.name, "Senior/Junior")
# for classes in courses:
#     if graph.nodes(classes):
#         graph.add_node(classes.name)


# for classes in courses:
#     if classes.prereq == "":
#         left_nodes.append(classes.name)
#     else:
#         for classes2 in courses:
#             if classes.prereq != "" and classes.name == classes2.prereq:
#                 middle_nodes.append(classes.name)
#             elif classes.prereq != "" and classes.name != classes2.prereq:
#                 right_nodes.append(classes)

#pos = nx.DiGraph({n: (0, i) for i, n in enumerate(left_nodes)})
#pos.update({n: (1, i + 0.5) for i, n in enumerate(middle_nodes)})
#pos.update({n: (2, i + 0.5) for i, n in enumerate(right_nodes)})

# plt.figure(1,figsize=(12,12))
# print(len(graph.nodes()))
# d = dict(graph.degree)
# list(nx.topological_sort(graph))
# plt.tight_layout()
# nx.draw(graph, with_labels=True,font_weight='bold', node_size=500)
# ax = plt.gca()
# ax.margins(0.01)
# plt.axis("off")
# plt.show()
# i = 0;
# list(reversed(list(nx.topological_sort(graph))))
# graph.edges()


# In[ ]:





# In[ ]:




