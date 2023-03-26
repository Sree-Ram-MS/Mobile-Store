from django import forms
from .models import Products

class ProductForm(forms.ModelForm):
    class Meta:
        model=Products
        exclude=[
            'user'
        ]

def clean(self):
    cleaned_data= super().clean()
    prize=cleaned_data.get("prize")