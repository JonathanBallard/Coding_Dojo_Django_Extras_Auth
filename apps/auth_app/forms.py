from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm



class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'



















