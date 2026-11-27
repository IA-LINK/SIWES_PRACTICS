from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Supervisor, Logbook, Attendance
from .forms import StudentForm, SupervisorForm, LogbookForm, AttendanceForm
from django.db.models import Count, Q

from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
 
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


def logbook_create(request):
    if request.method == 'POST':
        form = LogbookForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('logbook_list')
    else:
        form = LogbookForm()

    return render(request, 'students/logbook_form.html', {
        'form': form
    })


def logbook_list(request):
    logbooks = Logbook.objects.all().order_by('-date')

    return render(request, 'students/logbook_list.html', {
        'logbooks': logbooks
    })


def logbook_review(request, id):
    logbook = get_object_or_404(Logbook, id=id)

    if request.method == 'POST':
        status = request.POST.get('status')
        comment = request.POST.get('supervisor_comment', '')

        if status in ['Approved', 'Rejected']:
            logbook.status = status
            logbook.supervisor_comment = comment
            logbook.save()

            return redirect('logbook_list')

    return render(request, 'students/logbook_review.html', {
        'logbook': logbook
    })


def logbook_review(request, id):
    logbook = get_object_or_404(Logbook, id=id)

    if request.method == 'POST':
        status = request.POST.get('status')
        comment = request.POST.get('supervisor_comment', '')

        if status in ['Approved', 'Rejected']:
            logbook.status = status
            logbook.supervisor_comment = comment
            logbook.save()

            return redirect('logbook_list')

    return render(request, 'students/logbook_review.html', {
        'logbook': logbook
    })



def attendance_list(request):
    attendances = Attendance.objects.select_related('student').order_by('-date')

    return render(request, 'students/attendance_list.html', {
        'attendances': attendances
    })


def attendance_create(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('attendance_list')

    else:
        form = AttendanceForm()

    return render(request, 'students/attendance_form.html', {
        'form': form
    })


def attendance_update(request, id):
    attendance = get_object_or_404(Attendance, id=id)

    if request.method == 'POST':
        form = AttendanceForm(request.POST, instance=attendance)

        if form.is_valid():
            form.save()
            return redirect('attendance_list')

    else:
        form = AttendanceForm(instance=attendance)

    return render(request, 'students/attendance_form.html', {
        'form': form
    })


def attendance_delete(request, id):
    attendance = get_object_or_404(Attendance, id=id)

    if request.method == 'POST':
        attendance.delete()
        return redirect('attendance_list')

    return render(request, 'students/attendance_confirm_delete.html', {
        'attendance': attendance
    })


def attendance_dashboard(request):

    total_attendance = Attendance.objects.count()

    present_count = Attendance.objects.filter(
        status='Present'
    ).count()

    absent_count = Attendance.objects.filter(
        status='Absent'
    ).count()

    late_count = Attendance.objects.filter(
        status='Late'
    ).count()

    recent_attendance = Attendance.objects.select_related(
        'student'
    ).order_by('-date')[:10]

    context = {
        'total_attendance': total_attendance,
        'present_count': present_count,
        'absent_count': absent_count,
        'late_count': late_count,
        'recent_attendance': recent_attendance,
    }

    return render(
        request,
        'students/attendance_dashboard.html',
        context
    )


def attendance_report(request):
    attendances = Attendance.objects.select_related('student').all()

    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    status = request.GET.get('status')
    search = request.GET.get('search')

    if start_date:
        attendances = attendances.filter(date__gte=start_date)

    if end_date:
        attendances = attendances.filter(date__lte=end_date)

    if status:
        attendances = attendances.filter(status=status)

    if search:
        attendances = attendances.filter(
            Q(student__first_name__icontains=search) |
            Q(student__last_name__icontains=search) |
            Q(student__matric_number__icontains=search)
        )

    context = {
        'attendances': attendances.order_by('-date'),
        'start_date': start_date or '',
        'end_date': end_date or '',
        'selected_status': status or '',
        'search': search or '',
    }

    return render(request, 'students/attendance_report.html', context)

def export_attendance_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = (
        'attachment; filename="attendance_report.pdf"'
    )

    pdf = canvas.Canvas(response, pagesize=A4)

    width, height = A4

    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(50, height - 50, "SIWES ATTENDANCE REPORT")

    pdf.setFont("Helvetica", 9)

    y = height - 90

    pdf.drawString(40, y, "Student")
    pdf.drawString(180, y, "Matric Number")
    pdf.drawString(310, y, "Date")
    pdf.drawString(390, y, "Status")

    y -= 25

    attendances = Attendance.objects.select_related(
        'student'
    ).order_by('-date')

    for attendance in attendances:

        if y < 50:
            pdf.showPage()
            pdf.setFont("Helvetica", 9)
            y = height - 50

        pdf.drawString(
            40, y,
            f"{attendance.student.first_name} {attendance.student.last_name}"[:25]
        )

        pdf.drawString(
            180, y,
            attendance.student.matric_number[:20]
        )

        pdf.drawString(310, y, str(attendance.date))
        pdf.drawString(390, y, attendance.status)

        y -= 20

    pdf.save()

    return response