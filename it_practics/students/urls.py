from django.urls import path
from . import views

urlpatterns = [
     # Create student
    path('students/add/', views.student_create, name='student_create'),

    # Read students
    path('students/', views.student_list, name='student_list'),

    # update
    path('students/edit/<int:id>/', views.student_update, name='student_update'),
    # delete student
    path('delete/<int:id>/', views.student_delete, name='student_delete'),

    path('dashboard/', views.dashboard, name='dashboard'),
]
