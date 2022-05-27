from core.forms import LoginForm, SignForm
from django.contrib.auth import authenticate, logout, login
from django.shortcuts import redirect, render
from django.views.generic import View
from django.db.models import Value, CharField, Q
from itertools import chain
from following.models import Follower
from ticketing.models import Review, Ticket
from core.models import User


class LoginPage(View):
    template = "login.html"
    form = LoginForm

    def get(self, request, *args, **kwargs):
        form = self.form
        message = ''
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
        user = Follower.objects.filter(user_id__in=User.objects.filter(id=request.user.id)).values("followed_user_id")
        reviews = Review.objects.filter(Q(user_id__in=user) | Q(user=request.user))
        reviews = reviews.annotate(content_type=Value("REVIEW", CharField()))
        tickets = Ticket.objects.filter(Q(user_id__in=user) | Q(user=request.user))
        tickets = tickets.annotate(content_type=Value("TICKET", CharField()))
        posts = sorted(chain(reviews, tickets), key=lambda post: (post.time_created), reverse=True)
        all_tickets = Ticket.objects.all()
        all_reviews = Review.objects.all()
        return render(request, self.template, context={"posts": posts, 'tickets': all_tickets, 'reviews': all_reviews})
