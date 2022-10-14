import scheduleGenerator as gen
import fileReader as fr


fr.getUserTrack(fr.drop)
fr.getNeededClasses()
gen.scheduleCreate()

#Output Course Schedule File


for course in gen.courseArray:
    print("\n" + "Semester: " + str(gen.k) + " " + gen.season() + "\n")
    gen.k = gen.k + 1
    for i in course:
        print(i)
