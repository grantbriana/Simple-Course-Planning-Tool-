'''
TestDag3 tests the notListed() function 
Purpose: notListed() function checks if a class has a prerequisite within the same semester 
in order to avoid a logic error of an unmet prerequisite

'''

import DAG2 as dag
import fileReader as fr

tempArray = []
fr.populateCourseArray("version 0.2\Tracks\Software Systems Track.csv")

'''
test 1: 
CPSC 1301 is in tempArray.
CPSC 1301 is prerequisite of CPSC 1302.
Assert that CPSC1302 has a prereq. in the temporary array
'''
tempArray.append("CPSC 1301")
assert(dag.notListed("CPSC 1302",tempArray))

'''
test 2: 
CPSC 3175 is in tempArray.
CPSC 3175 is prerequisite of CPSC 4135.
Assert that 4135 has a prereq. in the temporary array
'''
tempArray.append("CPSC 3175")
assert(dag.notListed("CPSC 4135",tempArray))

'''
test 2: 
CPSC 4135's prerequisites are added to tempArray.
Assert that 4135 has a prereq. in the temporary array
'''
tempArray = []
course = dag.getCourseObj("CPSC 3125")
for i in course.prereq:
    tempArray.append(i)
assert(dag.notListed("CPSC 3125",tempArray))

'''
test 2: 
TempArray is empty
Assert that 4157 does NOT have any prerequisites in temporary array
'''
tempArray = []
assert(dag.notListed("CPSC 3125",tempArray) == False)