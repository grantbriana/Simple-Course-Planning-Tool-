import fileReader as fr

#Test getCourseObj(courseName) function: Tests retrieval of course object based on course name
def getCourseObj(courseName):
  foundCourse = None
  for course in fr.courses:
    if course.name == courseName:
      foundCourse = course

  return foundCourse

fr.populateCourseArray("version 0.2\Tracks\Software Systems Track.csv")
assert(getCourseObj("CPSC 1302").description == "Computer Science II")
assert(getCourseObj("CPSC 1301").description == "Computer Science I")
assert(getCourseObj("CPSC 2108").description == "Data Structures")
