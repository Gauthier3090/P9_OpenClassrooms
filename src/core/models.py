from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import AbstractUser
from django.db import models
from django import forms


class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50, unique=False)
    USERNAME_FIELD = "username"


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, widget= forms.TextInput(attrs={"placeholder": "Nom d'utilisateur"}), label="Nom d'utilisateur")
    password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={"placeholder": "Mot de passe"}), label="Mot de passe")

class SignForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'password')