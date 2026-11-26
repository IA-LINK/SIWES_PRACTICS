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

    # SUPERVISORS
    path('supervisors/', views.supervisor_list, name='supervisor_list'),
    path('supervisors/add/', views.supervisor_create, name='supervisor_create'),
    path('supervisors/edit/<int:id>/', views.supervisor_update, name='supervisor_update'),
    path('supervisors/delete/<int:id>/', views.supervisor_delete, name='supervisor_delete'),

]
