
from django.http import HttpResponse


def home(request):
    """
    Display the SIWES Management System homepage.
    """
    return HttpResponse(
        "<h1>Welcome to SIWES Management System</h1>"
        "<p>Django application is working successfully.</p>"
    )
