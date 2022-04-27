from following.forms import FollowersForm
from django.shortcuts import render
from django.views.generic import View
from core.models import User
from following.controllers import unfollow_user, username_exists, create_follower
from following.models import Follower


class FollowersPage(View):
    page = "followers.html"
    form = FollowersForm

    def get(self, request):
        form = self.form
        username = request.GET.get('unfollow')
        if username:
            unfollow_user(username)
        context = {
            "form": form,
            "followers": self.followers(request.user.id),
            "subscribers": self.subscribers(request.user.id)
        }
        print(context)
        return render(request, self.page, context=context)

    def post(self, request):
        form = self.form(request.POST)
        error = ""
        success = ""
        if form.is_valid():
            username = form.cleaned_data["username"]
            if username_exists(username):
                error = create_follower(username, request.user.id)
                if error == "":
                    success = "La personne a été rajoutée à vos abonnements !"
            else:
                error = "La personne n'existe pas. Veuillez réessayer !"
        context = {
            "form": form,
            "error": error,
            "success": success,
            "followers": self.followers(request.user.id),
            "subscribers": self.subscribers(request.user.id)
        }
        return render(request, self.page, context=context)

    @staticmethod
    def followers(user_id):
        tab = []
        followers = Follower.objects.all().filter(user_id=user_id)
        for follower in followers:
            tab.append(User.objects.get(id=follower.followed_user_id).username)
        return tab

    @staticmethod
    def subscribers(user_id):
        tab = []
        followers = Follower.objects.all().filter(followed_user_id=user_id)
        for follower in followers:
            tab.append(User.objects.get(id=follower.user_id).username)
        return tab
