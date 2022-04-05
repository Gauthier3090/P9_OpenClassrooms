"""
    Import modules
"""
from django.shortcuts import render


def index(request):
    """
        Return my template index.html
    """
    return render(request, "index.html")
