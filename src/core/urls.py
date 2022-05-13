from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import LoginPage, SignupPage, Logout, FluxPage, PostPage

urlpatterns = [
    path("login/", LoginPage.as_view(), name="login"),
    path("signup/", SignupPage.as_view(), name="signup"),
    path('logout/', Logout.as_view(), name="logout"),
    path('flux/', login_required(FluxPage.as_view()), name='flux'),
    path('posts/', login_required(PostPage.as_view()), name='posts'),
]
