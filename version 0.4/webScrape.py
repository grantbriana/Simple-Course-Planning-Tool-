#This is a test of web scraping

import urllib.request
# import json
import json
# store the URL in url as 

url = "https://catalog.columbusstate.edu/academic-units/business/computer-science/computer-science-bs-software-systems-track/"


def getResponse(url):
    operUrl = urllib.request.urlopen(url)
    if(operUrl.getcode()==200):
       data = operUrl.read()
    else:
       print("Error receiving data", operUrl.getcode())
    return data

def getResponse2(url):
    operUrl = urllib.request.urlopen(url)
    if(operUrl.getcode()==200):
        data = operUrl.read()
        jsonData = json.loads(data)
    else:
        print("Error receiving data", operUrl.getcode())
    return jsonData

def main():
    jsonData = getResponse(url)
    print(jsonData)

main()