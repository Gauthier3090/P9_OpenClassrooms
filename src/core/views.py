from core.forms import LoginForm, SignForm
from django.contrib.auth import authenticate, logout, login
from django.shortcuts import redirect, render
from django.views.generic import View


class LoginPage(View):
    template = "login.html"
    form = LoginForm

    def get(self, request):
        form = self.form
        message = ''
        if request.user.is_authenticated:
            logout(request)
        return render(request, self.template, context={"form": form, "message": message})

    def post(self, request):
        message = ''
        form = self.form(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data["username"], password=form.cleaned_data["password"],)
            if user is not None:
                login(request, user)
                return redirect('followers')
            message = "Identifiants invalides."
        return render(request, self.template, context={"form": form, "message": message})


class SignupPage(View):
    template = "signup.html"
    form = SignForm

    def get(self, request):
        form = self.form
        message = ''
        return render(request, self.template, context={"form": form, "message": message})

    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signup')
        return render(request, 'signup.html', context={'form': form})


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('login')
