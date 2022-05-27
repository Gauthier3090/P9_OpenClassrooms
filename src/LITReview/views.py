from django.shortcuts import render


def error_404_handler(request, exception):
    return render(request, '404.html', status=404)
