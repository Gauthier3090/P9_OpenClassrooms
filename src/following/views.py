from core.forms import FollowersForm
from django.shortcuts import redirect, render
from django.views.generic import View
from following.controllers import username_exists, createFollower


class FollowersPage(View):
    template = "followers.html"
    form = FollowersForm

    def get(self, request):
        form = self.form
        message = ''
        return render(request, self.template, context={"form": form, "message": message})

    def post(self, request):
        message = ''
        form = self.form(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            if username_exists(username):
                message = createFollower(username, request.user.id)
            else:
                message = "La personne n'existe pas. Veuillez réessayer !"
        return render(request, self.template, context={"form": form, "message": message})
