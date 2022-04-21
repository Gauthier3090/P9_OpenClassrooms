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
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', core.views.LoginPage.as_view(template="login.html"), name="login"),
    path('followers/', core.views.followers, name="followers"),
    path('logout/', core.views.logout_user, name="logout"),
    path('signup/', core.views.signup_page, name='signup'),
    path('admin/', admin.site.urls),
]
