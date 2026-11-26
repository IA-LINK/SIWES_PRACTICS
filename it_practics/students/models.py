
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
