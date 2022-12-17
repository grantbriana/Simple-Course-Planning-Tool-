import fileReader as fr
import scheduleGenerator as gen
import DAG as dag



def displaySchedule():
    schedule = ""
    for course in gen.courseArray:
        #print("\n" + "Semester: " + str(gen.k) + " " + gen.season() + "\n")
        schedule += "\n" + "Semester: " + str(gen.k) + " " + gen.season() + "\n"
        #gen.k += 1
        for i in course:
            #print(i)
            schedule += i + "\n"
        gen.k += 1
    return schedule

