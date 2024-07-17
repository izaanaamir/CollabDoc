from django.core.exceptions import ValidationError


class AtLeastOneSpecialCharacterValidator:
    def validate(self, password, user=None):
        if not any(
            char in "!@#$%^&*()-_=+[]{}|;:,.<>?/~`" for char in password
        ):
            raise ValidationError(
                "Password must contain at least one special character."
            )

    def get_help_text(self):
        return "Your password must contain at least one special character."
