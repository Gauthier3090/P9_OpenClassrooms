from django import template
from ticketing.models import Review


register = template.Library()


@register.simple_tag
def check_review(ticket_id: int):
    review = Review.objects.all().filter(ticket_id=ticket_id)
    if review.count() == 1:
        return True
    return False
