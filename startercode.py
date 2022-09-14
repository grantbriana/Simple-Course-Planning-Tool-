#!/usr/bin/env python
# coding: utf-8

# In[33]:


studentInfo = {}
semesterOne = {"CRN":[],"Course_Name":[], "Hours":[], "Availability" : [], "Prereqs": []}
semesterTwo = {"CRN":[],"Course_Name":[], "Hours":[], "Availability" : [], "Prereqs": []}
semesterThree = {"CRN":[],"Course_Name":[], "Hours":[], "Availability" : [], "Prereqs": []}

courseList = {"Course" : ["Computer Science", "Math Nerd"]}
def InfoHandler(Name, Input):
    realCourse = False
    for course in courseList["Course"]:
        if(Input == course):
            realCourse = True
    if realCourse == True:
        studentInfo["Name"] = Name
        studentInfo["Input"] = Input
    else:
            print("Course not real")
InfoHandler("Joe", "Math Nerd")
if not studentInfo:
    print("no info given for student.")
else:
    print(studentInfo)


# In[ ]:




