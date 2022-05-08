from django import forms


class TicketForm(forms.Form):
    title = forms.CharField(max_length=128, widget=forms.TextInput(
        attrs={"class": "form-control w-75 mt-3"}), label="Titre")
    description = forms.CharField(label='Description', max_length=8192, widget=forms.Textarea(
        attrs={"class": "form-control"}))
    image = forms.ImageField(required=False)


class ReviewForm(forms.Form):
    RATED = [('0', '- 0'), ('1', '- 1'), ('2', '- 2'), ('3', '- 3'), ('4', '- 4'), ('5', '- 5')]
    headline = forms.CharField(max_length=128, widget=forms.TextInput(
        attrs={"class": "form-control w-75 mt-3"}), label="Titre")
    rate = forms.CharField(label='Notes', widget=forms.RadioSelect(choices=RATED))
    comment = forms.CharField(label='Commentaire', max_length=2048, widget=forms.Textarea(
        attrs={"class": "form-control"}))
