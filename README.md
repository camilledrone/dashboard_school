# Dashboard_school
Dashboard with school data

## Context
Dashboards are visual representations of relevant information within a company or organization. These dashboards are often consulted from a web browser. The graphics are displayed using web technologies. These dashboards can be composed of textual and visual elements such as graphs or diagrams to represent databases.

## Objectives
The goal of the project is to create a dashboard based on data sets from an American university. These data sets contain the data of about 150 000 students in about 50 subjects: the grades of the students as well as their curriculum in order to project them in a dashboard. 
We are going to process data on these former students, analyze them and display them using a dashboard, with certain indicators such as: classification by subject, enrollment or even results by gender. This system will allow a global follow-up of the class and will help the new students in their orientation of the school curriculum. 
The objectives of this dashboard are that incoming students should be able to have a global view of the previous class as well as have access to the curricula of former students in order to better orient their future school choice.

## Realisation
The following features are realized:
 - F1 visualize the number of students in each subject
 - F2 visualize the percentage of success in each subject
 - F3 visualize the total number of students of the university
 - F6 visualize the percentage of global success in a subject 
 - F7 visualize the percentage of men and women in a subject 
 - F8 view the average grade in a subject over time 
 - F9 view the average score on the last ACT test by gender

The first step was to program a web server, for that the Python language was used and the framework (or development infrastructure) Flask [9]. Indeed, Python is very easy to use and pleasant to use.
Flask, unlike other frameworks, does not impose any structure; one can develop an entire application on a single file. Nevertheless, we have followed certain conventions: 
- Style sheets, scripts, images and other elements that will never be generated dynamically must be in the 'static' folder
- HTML files must be in the 'templates' folder
- The file 'school.py' contains the different routes of the application
With the help of the framework, the server is created (a local server here).

In the code the lines '@school.route(" / ")' are decorators. In Python, decorators are always located above a function definition, and are used to modify/complete the behavior of that function. With Flask, decorators are used to associate a URL with a function.
So all the URLs needed were created: 
- The home page: '/dashboard/'
- The page giving details about the school's GPA: '/dashboard/gpa/'
- The pages associated with each subject X: '/dashboard/X
To access these pages, a redirection system in the JavaScript script have been set up.

Finally, to launch the python program, theCommand prompt can be used, then we need to: 
- (1) Move to the folder containing the python file
- (2) type the command "set FLASK_APP=school.py"
- (3) type the command "flask run"

A point to improve: for the moment the data are entered manually, as well as the subject pages (for the moment there are only "MATHS" and "PHYSICS"). We can complete the python code to generate automatically the other pages.

