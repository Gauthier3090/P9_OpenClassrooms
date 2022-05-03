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
        form1 = ReviewForm(request.POST)
        form2 = TicketForm(request.POST)
        if form1.is_valid():
            print("ok")
        else:
            print("non ok")
        if form2.is_valid():
            print("ok 1")
        else:
            print("non ok")
        if form1.is_valid() and form2.is_valid():
            print("deux ok")
        return render(request, self.template, context={"form": form1, "review": form2})
