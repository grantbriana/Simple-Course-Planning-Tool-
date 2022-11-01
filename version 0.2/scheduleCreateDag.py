import fileReader as fr
import networkx as nx
import DAG2 as dag

courseArray = []
roots = []
for course in fr.courses:
    if course.prereq == "":
        roots.append(course)

def scheduleCreateDag():
    tempArray = []
    nextClasses = []
    j = 0
    for course in roots:
        if (j < 12):
            x = dict(nx.bfs_successors(dag.g, source=course.name, depth_limit=1))
            for key, item in x.items():
                for k in item:
                    nextClasses.append(k)
            tempArray.append(course)
            for course2 in fr.courses:
                if course.name == course2.name:
                    course2.taken = True
            j = j + course.hours
        elif not roots:
            break
    for i in tempArray:
        for k in roots:
            if i.name == k.name:
                roots.remove(k)
    courseArray.append(tempArray)
    if roots:
        for i in roots:
            nextClasses.append(i.name)
    working = True
    while working == True:
        j = 0
        tempArray = []
        nextClassesTemp = []

        for classes in nextClasses:
            for course in fr.courses:
                if classes == course.name:
                    if j < 12 and course.taken == False:
                        if course.fall == True:
                            print(course.fall, " ", course.name)
                            nextClassesTemp.append(course.name)
                            course.taken = True
                            tempArray.append(course)
                            j = j + course.hours
                            x = dict(nx.bfs_successors(dag.g, source=course.name, depth_limit=1))
                            for key, item in x.items():
                                for k in item:
                                    isInNextClasses = False
                                    for m in nextClasses:
                                        if k == m:
                                            isInNextClasses = True
                                    if isInNextClasses == False:
                                        nextClasses.append(k)
                    else:
                        break
        if not tempArray:
            break
        else:
            courseArray.append(tempArray)
        j = 0
        tempArray = []
        nextClassesTemp = []

        for classes in nextClasses:
            for course in fr.courses:
                if classes == course.name:
                    if j < 12 and course.taken == False:
                        if course.spring == True:
                            print(course.spring, " ", course.name)
                            nextClassesTemp.append(course.name)
                            course.taken = True
                            tempArray.append(course)
                            j = j + course.hours
                            x = dict(nx.bfs_successors(dag.g, source=course.name, depth_limit=1))
                            for key, item in x.items():
                                for k in item:
                                    isInNextClasses = False
                                    for m in nextClasses:
                                        if k == m:
                                            isInNextClasses = True
                                    if isInNextClasses == False:
                                        nextClasses.append(k)
                    else:
                        break
        if not tempArray:
            break
        else:
            courseArray.append(tempArray)
        j = 0
        tempArray = []
        nextClassesTemp = []

        for classes in nextClasses:
            for course in fr.courses:
                if classes == course.name:
                    if j < 12 and course.taken == False:
                        if course.summer == True:
                            print(course.summer, " ", course.name)
                            nextClassesTemp.append(course.name)
                            course.taken = True
                            tempArray.append(course)
                            j = j + course.hours
                            x = dict(nx.bfs_successors(dag.g, source=course.name, depth_limit=1))
                            for key, item in x.items():
                                for k in item:
                                    isInNextClasses = False
                                    for m in nextClasses:
                                        if k == m:
                                            isInNextClasses = True
                                    if isInNextClasses == False:
                                        nextClasses.append(k)
                    else:
                        break
        if not tempArray:
            break
        else:
            courseArray.append(tempArray)

print(courseArray)