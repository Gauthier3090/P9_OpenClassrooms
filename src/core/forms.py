from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={"placeholder": "Nom d'utilisateur", "class": "input-login"}),
        label="")
    password = forms.CharField(max_length=50, widget=forms.PasswordInput(
        attrs={"placeholder": "Mot de passe", "class": "input-login"}),
        label="")


class SignForm(UserCreationForm):
    username = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={"placeholder": "Nom d'utilisateur", "class": "input-login"}),
        label="")
    password1 = forms.CharField(label="", widget=forms.PasswordInput(
        attrs={"placeholder": "Mot de passe", "class": "input-login"}))
    password2 = forms.CharField(label="", widget=forms.PasswordInput(
        attrs={
            "placeholder": "Confirmez votre mot de passe",
            "class": "input-login"
        }))

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'password1', 'password2')


class FollowersForm(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={
            "placeholder": "Nom d'utilisateur",
            "class": "input-followers"}),
        label="")
