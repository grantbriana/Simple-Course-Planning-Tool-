#!/usr/bin/env python
# coding: utf-8

# In[41]:


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
        self.fall = fall
        # bool
        self.spring = spring
        # bool
        self.summer = summer
        # dict
        self.prereq = prereq
        # bool
        self.taken = taken

    # Created these functions to grab the information.
    def __str__(
            self):  # ----->This is a string. This will output all the info for a class. ex use / print(course[0])  or print(course[0].Name() for specific info
        return f'{self.name}, {self.description}, {self.hours}, {self.fall}, {self.spring}, {self.summer}, {self.prereq}, {self.taken}'

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

#pos = nx.DiGraph({n: (0, i) for i, n in enumerate(left_nodes)})
#pos.update({n: (1, i + 0.5) for i, n in enumerate(middle_nodes)})
#pos.update({n: (2, i + 0.5) for i, n in enumerate(right_nodes)})

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




