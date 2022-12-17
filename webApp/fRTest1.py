import json


drop = "Software Systems"
degreeWorksPath = ""
#each class a literal class with attributes course, descript., etc

def readJson():
   fileName = ""
   with open('upload.json', 'r') as openfile:
      # Reading from json file
      jsonFile = json.load(openfile)
      fileName = jsonFile["fileName"]
   return fileName

degreeWorksPath = readJson()
print(degreeWorksPath)
