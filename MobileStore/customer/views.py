from django.shortcuts import render
from django.views.generic import TemplateView
from store.models import Products

# Create your views here.
class CustHome(TemplateView):
    template_name="userpage.html"
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["products"]=Products.objects.all()
        return context
    