from django import forms
from .models import CustUser
from django.contrib.auth.forms import UserCreationForm

class RegForm(UserCreationForm):
    class Meta:
        model=CustUser
        fields=["first_name","last_name","email","phone","address","image"]