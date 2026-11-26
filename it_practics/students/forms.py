
from django import forms
from .models import Student

from .models import Supervisor



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