from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm


# CREATE STUDENT
def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()

    return render(request, 'students/student_form.html', {
        'form': form
    })


# READ STUDENTS
def student_list(request):
    students = Student.objects.all()

    return render(request, 'students/student_list.html', {
        'students': students
    })
    