import fileReader as fr
import scheduleGenerator2 as gen
import xlsxwriter
import DAG2 as dag


for course in gen.courseArray:
    print("\n" + "Semester: " + str(gen.k) + " " + gen.season() + "\n")
    #gen.k += 1
    for i in course:
        print(i)
    gen.k += 1


def writeSheet():
    # Workbook() takes one, non-optional, argument
    # which is the filename that we want to create.
    workbook = xlsxwriter.Workbook('generated_schedule.xlsx')
    
    # The workbook object is then used to add new
    # worksheet via the add_worksheet() method.
    worksheet = workbook.add_worksheet()
    
    row =  0
    column = 0

    for course in gen.courseArray:
        for i in course: 
            worksheet.write(row, column, i)
            row += 1

    row = 0
    column = 1

    for course in gen.courseArray:
        for i in course: 
            description = dag.getCourseObj(i).description
            worksheet.write(row, column, description)
            row += 1

    row = 0
    column = 2
    for course in gen.courseArray:
        for i in course: 
            hours = dag.getCourseObj(i).hours
            worksheet.write(row, column, hours)
            row += 1




    workbook.close()

writeSheet()