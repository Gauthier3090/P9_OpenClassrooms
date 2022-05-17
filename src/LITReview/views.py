from django.http import HttpResponseRedirect
from django.shortcuts import render


def index(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect("flux/")
    return render(request, "login.html")


def error_404_handler(request, exception):
    return render(request, '404.html', status=404)
