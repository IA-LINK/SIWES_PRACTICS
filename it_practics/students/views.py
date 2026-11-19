
from django.http import HttpResponse


def home(request):
    """
    Display the SIWES Management System homepage.
    """
    return HttpResponse(
        "<h1>Welcome to SIWES Management System</h1>"
        "<h2>JAMES AYIKA IKWOGYA 21/64858D/1</h2>"
        "<p>Django application is working successfully.</p>"
    )
