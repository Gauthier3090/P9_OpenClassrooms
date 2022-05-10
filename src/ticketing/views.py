import datetime

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View, UpdateView
from django.urls import reverse
from ticketing.forms import ReviewForm, TicketForm
from ticketing.models import Review, Ticket


class TicketModifyPage(UpdateView):
    model = Ticket
    fields = ["id"]
    form = TicketForm
    template = "modify-ticket.html"

    def get_success_url(self):
        return reverse('modify', args=(self.object.id,))


class ReviewPage(View):
    template = "review.html"

    def get(self, request):
        review_form = ReviewForm(request.GET)
        ticket_form = TicketForm(request.GET, request.FILES)
        return render(request, self.template, context={"ticket": ticket_form, "review": review_form})

    def post(self, request):
        error_review = ""
        error_ticket = ""
        success = ""
        review_form = ReviewForm(request.POST)
        ticket_form = TicketForm(request.POST, request.FILES)
        if review_form.is_valid() and ticket_form.is_valid():
            title = ticket_form.cleaned_data["title"]
            description = ticket_form.cleaned_data["description"]
            image = ticket_form.cleaned_data["image"]
            time_created = datetime.date.today()
            headline = review_form.cleaned_data["headline"]
            comment = review_form.cleaned_data["comment"]
            rate = review_form.cleaned_data["rate"]
            ticket = Ticket.objects.create(title=title, description=description, user=request.user,
                                           image=image, time_created=time_created)
            review = Review.objects.create(ticket=ticket, rating=rate, user=request.user, headline=headline,
                                           body=comment, time_created=time_created)
            ticket.save()
            review.save()
            success = "Votre critique a été sauvegardée !"
            review_form = ReviewForm()
            ticket_form = TicketForm()
        else:
            error_review = review_form.errors
            error_ticket = ticket_form.errors
        context = {
            "ticket": ticket_form,
            "review": review_form,
            "success": success,
            "error_review": error_review,
            "error_ticket": error_ticket
            }
        return render(request, self.template, context=context)
