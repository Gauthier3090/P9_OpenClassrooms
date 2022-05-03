from django.shortcuts import render
from django.views.generic import View
from ticketing.forms import ReviewForm, TicketForm

class ReviewPage(View):
    template = "review.html"

    def get(self, request):
        review_form = ReviewForm(request.GET, prefix="review")
        ticket_form = TicketForm(request.GET, prefix="ticket")
        return render(request, self.template, context={"ticket": ticket_form, "review": review_form})

    def post(self, request):
        review_form = ReviewForm(request.POST, prefix="review")
        ticket_form = TicketForm(request.POST, prefix="ticket")
        if all([review_form.is_valid(), ticket_form.is_valid()]):
            print("OK")
        else:
            print(review_form.is_valid(), ticket_form.is_valid())
            review_form = ReviewForm(prefix="review")
            ticket_form = TicketForm(prefix="ticket")
        return render(request, self.template, context={"ticket": ticket_form, "review": review_form})
