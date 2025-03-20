from django import forms
from phonenumber_field.formfields import PhoneNumberField
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    phone_number = PhoneNumberField(required=False)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name','email', 'phone_number', 'password1', 'password2']