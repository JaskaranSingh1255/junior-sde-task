I Have listed some of the steps below that we can follow to proceed with this project 

1 Tech Stack

- Django REST Framework
- PyMongo
- MongoDB (local)

 2 Setup Instructions
  List of dependecies
-Django==4.2.5
-djangorestframework==3.14.0
-pymongo==4.6.1
 3 Start MongoDB locally (default port 27017)
 4 run python manage.py runserver
 5 endpoints to run


-Create Employee	POST	/employees/
-Get Employee	GET	/employees/<employee_id>/
-Update Employee	PUT	/employees/<employee_id>/
-Delete Employee	DELETE	/employees/<employee_id>/
-List by Department	GET	/employees/?department=Engineering
-Average Salary	GET	/employees/avg-salary/
-Search by Skill	GET	/employees/search/?skill=Python
-Paginated Employees	GET	/employees/paginated/?page=1&size=5
-Search by Skill	GET	/employees/search/?skill=Python
-Paginated Employees	GET	/employees/paginated/?page=1&size=5
    
