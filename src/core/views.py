from core.forms import LoginForm, SignForm
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import View


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
                return redirect('home')
            message = "Identifiants invalides."
        return render(request, self.template, context={"form": form, "message": message})


def logout_user(request):
    logout(request)
    return redirect('login')


@login_required
def home(request):
    return render(request, "home.html")


def signup_page(request):
    form = SignForm()
    print(request.method)
    if request.method == 'POST':
        form = SignForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            print('success')
            return redirect(reverse('signup'))
    print('HELP')
    return render(request, 'signup.html', context={'form': form})
