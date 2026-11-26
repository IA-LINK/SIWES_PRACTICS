from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm
from .forms import SupervisorForm


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
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        student.delete()
        return redirect('student_list')

    return render(request, 'students/student_confirm_delete.html', {
        'student': student
    })



def dashboard(request):
    total_students = Student.objects.count()

    context = {
        'total_students': total_students,
        'total_supervisors': 0,
        'total_reports': 0,
        'total_departments': 0,
    }

    return render(request, 'students/dashboard.html', context)


def supervisor_list(request):
    supervisors = Supervisor.objects.all()

    return render(request, 'students/supervisor_list.html', {
        'supervisors': supervisors
    })


def supervisor_create(request):
    if request.method == 'POST':
        form = SupervisorForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('supervisor_list')
    else:
        form = SupervisorForm()

    return render(request, 'students/supervisor_form.html', {
        'form': form
    })


def supervisor_update(request, id):
    supervisor = get_object_or_404(Supervisor, id=id)

    if request.method == 'POST':
        form = SupervisorForm(request.POST, instance=supervisor)

        if form.is_valid():
            form.save()
            return redirect('supervisor_list')
    else:
        form = SupervisorForm(instance=supervisor)

    return render(request, 'students/supervisor_form.html', {
        'form': form
    })


def supervisor_delete(request, id):
    supervisor = get_object_or_404(Supervisor, id=id)

    if request.method == 'POST':
        supervisor.delete()
        return redirect('supervisor_list')

    return render(request, 'students/supervisor_confirm_delete.html', {
        'supervisor': supervisor
    })
