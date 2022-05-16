from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={"placeholder": "Nom d'utilisateur", "class": "form-control w-75 mb-2"}), label="")
    password = forms.CharField(max_length=50, widget=forms.PasswordInput(
        attrs={"placeholder": "Mot de passe", "class": "form-control w-75"}), label="")


class SignForm(UserCreationForm):
    username = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={"placeholder": "Nom d'utilisateur", "class": "form-control w-75"}), label="")
    password1 = forms.CharField(label="", widget=forms.PasswordInput(
        attrs={"placeholder": "Mot de passe", "class": "form-control w-75"}))
    password2 = forms.CharField(label="", widget=forms.PasswordInput(
        attrs={"placeholder": "Confirmez votre mot de passe", "class": "form-control w-75"}))

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'password1', 'password2')
