from core.forms import FollowersForm, LoginForm, SignForm
from django.contrib.auth import authenticate, logout, login
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import View
from core.validators import CheckUser


class LoginPage(View):
    template = "login.html"
    form = LoginForm

    def get(self, request):
        form = self.form
        message = ''
        return render(request, self.template, context={"form": form, "message": message})

    def post(self, request):
        message = ''
        form = self.form(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
                return redirect('followers')
            message = "Identifiants invalides."
        return render(request, self.template, context={"form": form, "message": message})


def logout_user(request):
    logout(request)
    return redirect('login')


class FollowersPage(View):
    template = "followers.html"
    form = FollowersForm

    def get(self, request):
        form = self.form
        message = ''
        return render(request, self.template, context={"form": form, "message": message})

    def post(self, request):
        message = ''
        follow = CheckUser
        form = self.form(request.POST)
        if form.is_valid():
            if follow.username_exists(form.cleaned_data["username"]):
                message = "La personne a été rajoutée à vos abonnements !"
                return redirect('followers'l)
            message = "La personne n'existe pas. Veuillez réessayer !"
        return render(request, self.template, context={"form": form, "message": message})


def signup_page(request):
    form = SignForm()
    if request.method == 'POST':
        form = SignForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('signup'))
    return render(request, 'signup.html', context={'form': form})
