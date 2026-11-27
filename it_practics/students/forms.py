
from django import forms
from .models import Student, Supervisor, Logbook, Attendance



class StudentForm(forms.ModelForm):
    """
    Form for creating and updating student records.
    """

    class Meta:
        model = Student

        fields = [
            'first_name',
            'last_name',
            'matric_number',
            'department',
            'institution',
            'email',
            'phone',
        ]

        widgets = {
            'first_name': forms.TextInput(
                attrs={'class': 'form-control'}
            ),

            'last_name': forms.TextInput(
                attrs={'class': 'form-control'}
            ),

            'matric_number': forms.TextInput(
                attrs={'class': 'form-control'}
            ),

            'department': forms.TextInput(
                attrs={'class': 'form-control'}
            ),

            'institution': forms.TextInput(
                attrs={'class': 'form-control'}
            ),

            'email': forms.EmailInput(
                attrs={'class': 'form-control'}
            ),

            'phone': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
        }

class SupervisorForm(forms.ModelForm):
    class Meta:
        model = Supervisor
        fields = [
            'full_name',
            'email',
            'phone',
            'department',
            'designation',
        ]

class LogbookForm(forms.ModelForm):
    class Meta:
        model = Logbook
        fields = [
            'student',
            'supervisor',
            'date',
            'activities',
            'skills_learned',
            'challenges',
        ]

        widgets = {
            'date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'activities': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4
            }),
            'skills_learned': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3
            }),
            'challenges': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3
            }),
        }



class AttendanceForm(forms.ModelForm):

    class Meta:
        model = Attendance
        fields = [
            'student',
            'time_in',
            'time_out',
            'status',
            'remarks',
        ]

        widgets = {
            'student': forms.Select(attrs={
                'class': 'form-control'
            }),

            'time_in': forms.TimeInput(attrs={
                'class': 'form-control',
                'type': 'time'
            }),

            'time_out': forms.TimeInput(attrs={
                'class': 'form-control',
                'type': 'time'
            }),

            'status': forms.Select(attrs={
                'class': 'form-control'
            }),

            'remarks': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3
            }),
        }
