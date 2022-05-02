from django.shortcuts import render
from django.views.generic import View
from ticketing.forms import ReviewForm, TicketForm

class ReviewPage(View):
    template = "review.html"
    form = TicketForm
    form_review = ReviewForm

    def get(self, request):
        return render(request, self.template, context={"form": self.form, "review": self.form_review})

    def post(self, request):
        return render(request, self.template, context={"form": self.form, "review": self.form_review})
