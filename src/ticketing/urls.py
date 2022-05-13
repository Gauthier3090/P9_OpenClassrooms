from django.urls import path
from .views import TicketModifyPage, ReviewPage
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("review/create/", login_required(ReviewPage.as_view()), name="review"),
    path('ticket/<pk>/edit/', login_required(TicketModifyPage.as_view()), name='modify'),
]
