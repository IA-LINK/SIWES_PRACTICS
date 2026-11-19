
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    """
    Display the SIWES Management System homepage.
    """
    return render(request, 'students/home.html')