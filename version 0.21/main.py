
import fileReader as fr
import scheduleGenerator2 as gen

for course in gen.courseArray:
    print("\n" + "Semester: " + str(gen.k) + " " + gen.season() + "\n")
    #gen.k += 1
    for i in course:
        print(i)
    gen.k += 1