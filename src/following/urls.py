from django.urls import path
from .views import FollowersPage
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("followers/", login_required(FollowersPage.as_view()), name="followers"),
]
