from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class CustHome(TemplateView):
    template_name="userpage.html"