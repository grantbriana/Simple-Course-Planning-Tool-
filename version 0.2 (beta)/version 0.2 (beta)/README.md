# Simple-Course-Planning-Tool-

## Background.
* Academic advising, especially properly planning courses across semesters to ensure students graduate on time, requires significant time and effort from both students and faculty. By collaboration between faculty of computer science and mathematics department, we are planning to build a Python-based smart class planning tool, which can be executed on any platform such as Windows, Linux, etc., or integrated into D2L as a third-party plug-in. 
* It is important for students to enroll in the proper courses designed to meet the degree requirements. Many students mistakenly enroll in classes simply because the classes fit their schedule without considering factors such as prerequisite requirements and different course offering times over the academic year semesters.
## Project Overview.
This smart advising tool can output a recommended class plan for a student to follow until the student’s graduation based on the student’s career goal, program interests, expected graduation date, etc. This software requires three inputs to generate an output excel form where recommended classes for different semesters are listed. The first input is the list of courses a student still needs until the student’s graduation, which will be obtained from Degreeworks as a pdf document. The second input is the prerequisite graph of all the required classes from the students’ track, which can be represented as a directed acyclic graph (DAG). The last input is the class schedule, which indicates when the student's required courses will be offered. 
** Please note:
1. the second and the third input can be found and obtained from CSU’s website. 
2. In computer science and mathematics, a directed acyclic graph (DAG) is a graph that is directed and without cycles connecting the other edges. This means that it is impossible to traverse the entire graph starting at one edge. The edges of the directed graph only go one way. The graph is a topological sorting, where each node is in a certain order.
* AI techniques can achieve state-of-the-art accuracy, sometimes exceeding human-level performance. AI is now a key technology behind driverless cars, enabling them to recognize a stop sign, or to distinguish a pedestrian from a lamppost. It’s achieving results that were not possible before. We will train AI models by our academic advising records. Figure 1 shows the model architecture.
## Requirements
Academic advising takes a long time for both students and faculty, especially when checking prerequisite issues. To facilitate class planning, we are to build a python based standalone application, which can be executed on the Windows platform.

### Functional requirements:
* The first goal of the software is to plan out classes among different semesters for a student until his/her graduation. The software takes three inputs and outputs an excel form where recommenced classes are listed. The 1st input is the classes a student must take before his/her graduation. The 2nd input is the prerequisite graph of all the required classes from the students’ track (may reflect the prerequisite with the DAG graph). The 3rd input is the class schedule, which indicates when the student's required courses will be offered. The recommended plan should be outputted by the software in the form of an excel document. 

* Another function of the software is to detect if a student’s plan has prerequisite issues. To do this, two inputs should be considered. One input is the prerequisite graph of all the required classes from the students’ track (may reflect the prerequisite with the DAG graph). Another is a class plan (i.e., an excel document).

* We should leverage AI/Machine learning algorithms to make the tool smarter. This part will be implemented in the second half of our semester. 

### Non-functional requirements (constrains):
* The software should be configurable. Specifically, the inputs must be separated from the software and be parsed by the software.

* The software should be implemented in Python and thus can be executed on Windows.



HOW TO RUN APP:

- We recommend creating a virtual environment to avoid conflicting versions of dependencies on your system
    - python -m venv venv 
    - venv\Scripts\activate  

- Install dependencies from requirements.txt
    - pip install -r requirements.txt  

- Run main.py path from command line or ide