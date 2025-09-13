# Junior SDE-I Task (Django + PyMongo)

This is a backend API built using Django REST Framework and PyMongo for the Junior SDE-I assignment. It supports basic CRUD operations and bonus features like pagination, skill-based search, and average salary aggregation.

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


Create Employee	POST	/employees/
Get Employee	GET	/employees/<employee_id>/
Update Employee	PUT	/employees/<employee_id>/
Delete Employee	DELETE	/employees/<employee_id>/
List by Department	GET	/employees/?department=Engineering
Average Salary	GET	/employees/avg-salary/
Search by Skill	GET	/employees/search/?skill=Python
Paginated Employees	GET	/employees/paginated/?page=1&size=5
Search by Skill	GET	/employees/search/?skill=Python
Paginated Employees	GET	/employees/paginated/?page=1&size=5
    
