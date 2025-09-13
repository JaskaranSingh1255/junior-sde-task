from django.urls import path
from . import views

urlpatterns = [
    path('employees', views.create_employee),
    path('employees/<str:employee_id>', views.get_employee),
    path('employees/<str:employee_id>', views.update_employee),
    path('employees/<str:employee_id>', views.delete_employee),
    path('employees/search/', views.search_by_skill),
    path('employees/avg-salary/', views.avg_salary),
    path('employees/', views.list_by_department),
    path('employees/paginated/', views.paginated_employees),
]
