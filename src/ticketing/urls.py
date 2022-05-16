from django.urls import path
from .views import TicketModifyPage, ReviewPage, ReviewModifyPage, ReviewDeletePage, TicketDeletePage, CreateReview
from .views import CreateTicket
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("review/create/", login_required(ReviewPage.as_view()), name="user-review"),
    path("ticket/create/", login_required(CreateTicket.as_view()), name="create-ticket"),
    path('ticket/<pk>/edit/', login_required(TicketModifyPage.as_view()), name="edit-ticket"),
    path('review/<pk>/edit/', login_required(ReviewModifyPage.as_view()), name="edit-review"),
    path('ticket/<pk>/delete/', login_required(TicketDeletePage.as_view()), name="delete-ticket"),
    path('review/<pk>/delete/', login_required(ReviewDeletePage.as_view()), name="delete-review"),
    path('review/<pk>/create/', login_required(CreateReview.as_view()), name="create-review"),
]
