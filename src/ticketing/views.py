import datetime
from django.shortcuts import render
from django.views.generic import View, UpdateView
from .forms import ReviewForm, TicketForm
from .models import Review, Ticket


class ReviewModifyPage(UpdateView):
    model = Review
    fields = ['headline', 'rating', 'body']
    template_name = "modify-review.html"
    object = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        review = Review.objects.get(id=self.object.pk)
        ticket = Ticket.objects.get(review__user_id=review.id)
        context['review'] = review
        context['ticket'] = ticket
        return context

    def post(self, request, **kwargs):
        review_form = ReviewForm(request.POST)
        self.object = self.get_object()
        if review_form.is_valid():
            title = review_form.cleaned_data["title"]
            rate = review_form.cleaned_data["rate"]
            comment = review_form.cleaned_data["comment"]
            Review.objects.filter(id=self.object.id).update(headline=title, rating=rate, body=comment)
        else:
            print(review_form.errors)
        return super(ReviewModifyPage, self).post(request, **kwargs)


class TicketModifyPage(UpdateView):
    model = Ticket
    fields = ['title', 'description', 'image']
    template_name = "modify-ticket.html"
    object = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ticket = Ticket.objects.get(id=self.object.pk)
        context['ticket'] = ticket
        return context

    def post(self, request, **kwargs):
        ticket_form = TicketForm(request.POST, request.FILES)
        self.object = self.get_object()
        if ticket_form.is_valid():
            title = ticket_form.cleaned_data["title"]
            description = ticket_form.cleaned_data["description"]
            image = ticket_form.cleaned_data["image"]
            if image is None:
                image = self.object.image
            Ticket.objects.filter(id=self.object.id).update(title=title, description=description, image=image)
        else:
            print(ticket_form.errors)
        return super(TicketModifyPage, self).post(request, **kwargs)


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
