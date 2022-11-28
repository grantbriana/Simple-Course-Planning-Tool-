import DAG2 as dag

#Test BFS
#Iterate through untaken path. Check if all class prerequisites are taken before course position
for u in dag.objpath:
  assert(dag.prereqCheck(u.name) or dag.lessThan(u.name) == False, "Error in graph traversal: Prerequisite not satisfied")