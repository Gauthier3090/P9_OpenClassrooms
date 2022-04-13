import code
from django.core.exceptions import ValidationError

class CheckLetter:
    def validate(self, password, user=None):
        if not any(char.isalpha() for char in password):
            raise ValidationError('Le mot de passe doit contenir une lettre', code='password_no_letters')
    
    def get_help_text(self):
        return 'Votre mot de passe doit contenir au moins une majuscule ou minuscule.'


class CheckNumber:
    def validate(self, password, user=None):
        if not any(char.isdigit() for char in password):
            raise ValidationError('Le mot de passe doit contenir un chiffre', code='password_no_numbers')
    
    def get_help_text(self):
        return 'Votre mot de passe doit contenir au moins un chiffre.'