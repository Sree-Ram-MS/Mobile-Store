from django import forms
from .models import CustUser
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

class RegForm(UserCreationForm):
    class Meta:
        model=CustUser
        fields=["first_name","last_name","email","phone","address","image","username","usertype","password1","password2"]
        help_texts={
            'username':None
        }

class LogForm(AuthenticationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))