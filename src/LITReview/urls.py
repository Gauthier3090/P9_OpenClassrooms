"""LITReview URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import core.views
import following.views
from django.contrib import admin
from django.urls import path
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', core.views.LoginPage.as_view(), name="login"),
    path('followers/', login_required(following.views.FollowersPage.as_view()), name="followers"),
    path('logout/', core.views.Logout.as_view(), name="logout"),
    path('signup/', core.views.SignupPage.as_view(), name='signup'),
    path('admin/', admin.site.urls),
]
