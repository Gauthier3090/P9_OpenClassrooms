from unicodedata import name
from django import forms


class TicketForm(forms.Form):
    title = forms.CharField(max_length=128, widget=forms.TextInput(
        attrs={"class": "form-control w-75 mt-3"}), label="Titre")
    description = forms.CharField(label='Description', max_length=100, widget=forms.Textarea(
        attrs={"class": "form-control"}))
    image = forms.ImageField(widget=forms.FileInput(
        attrs={"class": "form-control mt-3"}), label="Image")


class ReviewForm(forms.Form):
    RATED = [('0', '- 0'), ('1', '- 1'), ('2', '- 2'), ('3', '- 3'), ('4', '- 4'), ('5', '- 5')]
    title = forms.CharField(max_length=128, widget=forms.TextInput(
        attrs={"class": "form-control w-75 mt-3"}), label="Titre")
    rate = forms.CharField(label='Notes', widget=forms.RadioSelect(choices=RATED))
    comment = forms.CharField(label='Commentaire', max_length=100, widget=forms.Textarea(
        attrs={"class": "form-control"}))
