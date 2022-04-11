from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, widget= forms.TextInput(attrs={"placeholder": "Nom d'utilisateur"}), label="Nom d'utilisateur")
    password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={"placeholder": "Mot de passe"}), label="Mot de passe")

class SignForm(UserCreationForm):
    password1 = forms.CharField(label=("Password"),
        widget=forms.PasswordInput(attrs={"placeholder": "Mot de passe"}))
    password2 = forms.CharField(label=("Password confirmation"),
        widget=forms.PasswordInput(attrs={"placeholder": "Confirmez votre mot de passe"}))
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username',)
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Entrez votre pseudo',
            })
        }