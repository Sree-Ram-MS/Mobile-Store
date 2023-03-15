from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView,CreateView
from .forms import RegForm
from .models import CustUser

# Create your views here.
class Homepage(TemplateView):
    template_name="Homepage.html"

class Reg(CreateView):
    template_name="Reg.html"
    form_class=RegForm
    model=CustUser
    success_url=reverse_lazy("Homepage")