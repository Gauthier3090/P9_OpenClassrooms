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
from django.conf import settings
from django.conf.urls.static import static
import core.views
import following.views
import ticketing.views
from django.contrib import admin
from django.urls import path
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('login/', core.views.LoginPage.as_view(), name="login"),
    path('followers/', login_required(following.views.FollowersPage.as_view()), name="followers"),
    path('logout/', core.views.Logout.as_view(), name="logout"),
    path('signup/', core.views.SignupPage.as_view(), name='signup'),
    path('review/', login_required(ticketing.views.ReviewPage.as_view()), name='review'),
    path('<pk>/modify/', login_required(ticketing.views.TicketModifyPage.as_view()), name='modify'),
    path('flux/', login_required(core.views.FluxPage.as_view()), name='flux'),
    path('posts/', login_required(core.views.PostPage.as_view()), name='posts'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
