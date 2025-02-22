from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    id = forms.IntegerField()
    ssn = forms.IntegerField()
    phone = forms.IntegerField()
    emergency_contact = forms.IntegerField()
    picture = forms.ImageField()

    class Meta:
        model = User
        fields = ['username', 'email', 'id', 'ssn', 'phone', 'emergency_contact', 'picture']