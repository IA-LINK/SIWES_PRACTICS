
from django.contrib import admin
from .models import Student
from .models import Supervisor
from .models import Attendance

admin.site.register(Attendance)
admin.site.register(Supervisor)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'matric_number',
        'department',
        'institution',
        'email',
    )

    search_fields = (
        'first_name',
        'last_name',
        'matric_number',
        'email',
    )

    list_filter = (
        'department',
        'institution',
    )
