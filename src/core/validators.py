from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model


class CheckLetter:
    def validate(self, password, user=None) -> ValidationError:
        if not any(char.isalpha() for char in password):
            raise ValidationError('Le mot de passe doit contenir une lettre', code='password_no_letters')

    def get_help_text(self) -> str:
        return 'Votre mot de passe doit contenir au moins une majuscule ou minuscule.'


class CheckNumber:
    def validate(self, password, user=None) -> ValidationError:
        if not any(char.isdigit() for char in password):
            raise ValidationError('Le mot de passe doit contenir un chiffre', code='password_no_numbers')

    def get_help_text(self) -> str:
        return 'Votre mot de passe doit contenir au moins un chiffre.'


class CheckUser:
    def username_exists(username) -> bool:
        User = get_user_model()
        if User.objects.filter(username=username).exists():
            return True
        return False
