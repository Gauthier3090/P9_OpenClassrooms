from core.forms import FollowersForm
from django.shortcuts import render
from django.views.generic import View

from core.models import User
from following.controllers import username_exists, create_follower
from following.models import Follower


class FollowersPage(View):
    template = "followers.html"
    form = FollowersForm

    def get(self, request):
        form = self.form
        error = ''
        return render(
            request,
            self.template,
            context={
                "form": form,
                "message": error,
                "followers": self.all_followers(request.user.id)
            }
        )

    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            if username_exists(username):
                error = create_follower(username, request.user.id)
            else:
                error = "La personne n'existe pas. Veuillez réessayer !"
            return render(
                request,
                self.template,
                context={
                    "form": form,
                    "message": error,
                    "followers": self.all_followers(request.user.id)
                }
            )

    @staticmethod
    def all_followers(user_id):
        tab = []
        followers = Follower.objects.all().filter(user_id=user_id)
        for follower in followers:
            tab.append(User.objects.get(id=follower.followed_user_id).username)
        return tab
