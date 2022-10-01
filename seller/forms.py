from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length= 100)
    last_name = forms.CharField(max_length= 100)
    email = forms.EmailField()

    def save(self, *args, **kwargs):
        user = super().save(*args, **kwargs)
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        return user


