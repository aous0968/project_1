from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField


class CustomAuthenticationForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(CustomAuthenticationForm, self).__init__(*args, **kwargs)

    username = UsernameField(widget=forms.TextInput(attrs={
        "autofocus": True,
        "class" : "form-control",
        }))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "autocomplete": "current-password",
            "class": "form-control",
        }),
    )


class RegisterForm(forms.Form):
    first_name = forms.CharField(
        label="First name", max_length=150, required=True)
    last_name = forms.CharField(label="Last name", max_length=150)
    email = forms.EmailField(required=True)
    password = forms.PasswordInput()
    confirm_password = forms.PasswordInput()

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )
