from django import forms


class FollowersForm(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={"placeholder": "Nom d'utilisateur", "class": "form-control w-75 mt-3"}), label="")
