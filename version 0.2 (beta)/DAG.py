import fileReader as fr
import networkx as nx
from matplotlib import pyplot as plt
#import numpy as np
from networkx.drawing.nx_pydot import graphviz_layout
import scheduleGenerator as generator
#from xlwt import Workbook
import xlwt 
import scheduleGenerator as generator
#wb = Workbook()




'''
nodes = courses (ex. ['CPSC 1301', 'CPSC 1302', 'CPSC 2108', ...])
edges = course prerequisite (ex['','CPSC 1301'] ['CPSC 1301','CPSC 1302'] ['CPSC 1301','CPSC 2108'])
'''

#------------------------------------------------------------DAG tree
# group nodes by column
left_nodes = []
middle_nodes = []
right_nodes = []

graph = nx.DiGraph()
graph.add_node("Senior")
graph.add_node("Senior/Junior")

for course in fr.courses:
    graph.add_node(str(course.name))
j = 0
for classes in fr.courses:
    for classes2 in fr.courses:
        if classes2.prereq == classes.name:
            graph.add_edge(classes.name, classes2.name)
        elif classes.prereq == "Senior":
            graph.add_edge(classes.name, "Senior")
        elif classes.prereq == "Senior/Junior":
            graph.add_edge(classes.name, "Senior")
            graph.add_edge(classes.name, "Senior/Junior")
for classes in fr.courses:
    if graph.nodes(classes):
        graph.add_node(classes.name)


for classes in fr.courses:
    if classes.prereq == "":
        left_nodes.append(classes.name)
    else:
        for classes2 in fr.courses:
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
plt.savefig("DAG.png")
plt.show()
i = 0;
list(reversed(list(nx.topological_sort(graph))))
graph.edges()
'''
j =0
sheet1 = wb.add_sheet('Sheet 1')
for i in generator.courseArray:
    for k in i:
        sheet1.write(j, 0, k.name)
        sheet1.write(j, 1, k.description)
        sheet1.write(j, 2, str(k.hours))
        sheet1.write(j, 3, k.prereq)
        j = j + 1
    j = j + 1

wb.save('SCP_Tool_output.xls')
'''