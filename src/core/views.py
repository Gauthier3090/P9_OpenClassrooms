from email import message
from django.views.generic import View
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from core.models import LoginForm

# Create your views here.

class LoginPage(View):
    template = "login.html"
    form = LoginForm

    def get(self, request):
        form = self.form
        message = ''
        return render(request, self.template, context={"form": form, "message": message})

    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            user = authenticate(
                username = form.cleaned_data["username"],
                password = form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
                return redirect('home')
            message = "Identifiants invalides."
        return render(request, self.template, context={"form": form, "message": message})

def logout_user(request):
    logout(request)
    return redirect('login')

@login_required
def home(request):
    return render(request, "home.html")
