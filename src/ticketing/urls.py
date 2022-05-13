from django.urls import path
from .views import TicketModifyPage, ReviewPage, ReviewModifyPage, ReviewDeletePage, TicketDeletePage
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("review/create/", login_required(ReviewPage.as_view()), name="review"),
    path('ticket/<pk>/edit/', login_required(TicketModifyPage.as_view()), name="edit-ticket"),
    path('review/<pk>/edit/', login_required(ReviewModifyPage.as_view()), name="edit-review"),
    path('ticket/<pk>/delete/', login_required(TicketDeletePage.as_view()), name="delete-ticket"),
    path('review/<pk>/delete/', login_required(ReviewDeletePage.as_view()), name="delete-review"),
]
