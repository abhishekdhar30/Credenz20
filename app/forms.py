from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254)
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    phone_number=forms.IntegerField()

    class Meta:
        model = User
        fields = ('username', 'email' ,'first_name', 'last_name', 'phone_number', 'password1', 'password2', )
        help_texts = {
            'username' : None,
            'password1' : None,
        }
