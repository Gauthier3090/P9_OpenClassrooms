from core.forms import LoginForm, SignForm
from django.contrib.auth import authenticate, logout, login
from django.shortcuts import redirect, render
from django.views.generic import View
from django.db.models import Value, CharField
from itertools import chain
from ticketing.models import Review, Ticket


class LoginPage(View):
    template = "login.html"
    form = LoginForm

    def get(self, request, *args, **kwargs):
        form = self.form
        message = ''
        if request.user.is_authenticated:
            logout(request)
        return render(request, self.template, context={"form": form, "message": message})

    def post(self, request, *args, **kwargs):
        message = ''
        form = self.form(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data["username"], password=form.cleaned_data["password"],)
            if user is not None:
                login(request, user)
                return redirect("flux")
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
        message = ""
        if form.is_valid():
            form.save()
            message = "Votre compte a été enregistré"
        return render(request, self.template, context={"form": form, "message": message})


class Logout(View):
    @staticmethod
    def get(request):
        logout(request)
        return redirect('login')


class PostPage(View):
    template = "posts.html"

    def get(self, request):
        reviews = Review.objects.all()
        tickets = Ticket.objects.all()
        return render(request, self.template, context={"tickets": tickets, "reviews": reviews})


class FluxPage(View):
    template = "flux.html"

    def get(self, request):
        reviews = Review.objects.annotate(content_type=Value("REVIEW", CharField()))
        tickets = Ticket.objects.annotate(content_type=Value("TICKET", CharField()))
        posts = sorted(chain(reviews, tickets), key=lambda post: post.time_created, reverse=True)
        return render(request, self.template, context={'posts': posts, 'tickets': tickets})
