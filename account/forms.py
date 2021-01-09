from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,

)
User = get_user_model()

USER_TYPES =(
    ('customer', 'Customer'),
    ('car_dealer', 'Car Dealer'),
)

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, help_text='First Name')
    last_name = forms.CharField(max_length=100, help_text='Last Name')
    email = forms.EmailField(max_length=150, help_text='Email')
    type = forms.ChoiceField(choices=USER_TYPES, help_text='User Type')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'type','password1', 'password2')


class PasswordResetRequestForm(forms.Form):
    email_or_username = forms.CharField(label=("Email Or Username"), max_length=254)


