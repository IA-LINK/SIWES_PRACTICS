from django.urls import path
from . import views

urlpatterns = [
     # Create student
    path('students/add/', views.student_create, name='student_create'),

    # Read students
    path('students/', views.student_list, name='student_list'),

]
