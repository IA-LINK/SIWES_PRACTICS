
from django.db import models


class Student(models.Model):
    """
    Store student information for the SIWES system.
    """

    first_name = models.CharField(max_length=100)

    last_name = models.CharField(max_length=100)

    matric_number = models.CharField(
        max_length=30,
        unique=True
    )

    department = models.CharField(max_length=100)

    institution = models.CharField(max_length=150)

    email = models.EmailField(unique=True)

    phone = models.CharField(max_length=20)

    date_registered = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Supervisor(models.Model):
    full_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    department = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name


class Logbook(models.Model):

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE
    )

    supervisor = models.ForeignKey(
        Supervisor,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    date = models.DateField()
    activities = models.TextField()
    skills_learned = models.TextField(blank=True)
    challenges = models.TextField(blank=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    supervisor_comment = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student} - {self.date}"

class Attendance(models.Model):

    STATUS_CHOICES = [
        ('Present', 'Present'),
        ('Absent', 'Absent'),
        ('Late', 'Late'),
    ]

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='attendance_records'
    )

    date = models.DateField()

    time_in = models.TimeField(
        null=True,
        blank=True
    )

    time_out = models.TimeField(
        null=True,
        blank=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Present'
    )

    remarks = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['student', 'date'],
                name='unique_student_attendance_per_day'
            )
        ]

    def __str__(self):
        return f"{self.student} - {self.date} - {self.status}"


class Attendance(models.Model):
    """
    Store student attendance records.
    """

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='attendance_records'
    )

    date = models.DateField(auto_now_add=True)

    time_in = models.TimeField(null=True, blank=True)

    time_out = models.TimeField(null=True, blank=True)

    status = models.CharField(
        max_length=20,
        choices=[
            ('Present', 'Present'),
            ('Absent', 'Absent'),
            ('Late', 'Late'),
        ],
        default='Present'
    )

    remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.student} - {self.date}"
