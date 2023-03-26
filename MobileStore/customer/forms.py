from django import forms
from.models import *

class Confirmation(forms.Form):
    quantity=forms.IntegerField()
    city=forms.CharField(max_length=100)
    post=forms.CharField(max_length=100)
    pin=forms.IntegerField()


class PurchaseForm(forms.ModelForm):
    class Meta:
        model=Purchase
        exclude=[
            "mobile",
            "user"]

class ReviewForm(forms.ModelForm):
    class Meta:
        model=Review
        fields=["comment"]