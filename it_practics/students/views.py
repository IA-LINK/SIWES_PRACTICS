from django.shortcuts import render, redirect, get_object_or_404
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
    


# UPDATE STUDENT
def student_update(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)

        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)

    return render(request, 'students/student_update.html', {
        'form': form,
        'student': student
    })

# DELETE STUDENT
def student_delete(request, id):
    student = get_object_or_404(student, id=id)

    if request.method == 'POST':
        student.delete()
        return redirect('student_list')

    return render(request, 'students/student_confirm')