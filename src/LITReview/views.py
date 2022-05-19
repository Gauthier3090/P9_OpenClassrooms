from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render


def index(request):
    if request.user.is_authenticated:
        return redirect("flux")
    return render(request, "login.html")


def error_404_handler(request, exception):
    return render(request, '404.html', status=404)
