from core.forms import FollowersForm
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
        error = ''
        username = request.GET.get('unfollow')
        if username:
            error = unfollow_user(username)
        print(error)
        context = {
            "form": form,
            "error": error,
            "items": self.all(request.user.id),
            "followers": self.who_follow_me(request.user.id)
        }
        return render(request, self.page, context=context)

    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            if username_exists(username):
                error = create_follower(username, request.user.id)
            else:
                error = "La personne n'existe pas. Veuillez réessayer !"
        return render(request, self.page, context={"form": form, "message": error, "items": self.all(request.user.id)})

    @staticmethod
    def all(user_id):
        tab = []
        followers = Follower.objects.all().filter(user_id=user_id)
        for follower in followers:
            tab.append(User.objects.get(id=follower.followed_user_id).username)
        return tab

    @staticmethod
    def who_follow_me(user_id):
        tab = []
        followers = Follower.objects.all().filter(followed_user_id=user_id)
        for follower in followers:
            tab.append(User.objects.get(id=follower.user_id).username)
        return tab
