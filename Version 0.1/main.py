import scheduleGenerator as gen
import fileReader as fr


fr.getUserTrack(fr.drop)
fr.getNeededClasses()
gen.scheduleCreate()


k = gen.k
for course in gen.courseArray:
    print("\n" + "Semester: " + str(k) + " " + gen.season() + "\n")
    k = k + 1
    for i in course:
        print(i)