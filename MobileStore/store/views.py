from django.shortcuts import render
from django.views.generic import TemplateView,CreateView
from .models import Products
from .forms import *
from django.urls import reverse_lazy


# Create your views here.
class DealerHome(TemplateView):
    template_name="dealerpage.html"
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["products"]=Products.objects.all()
        return context
    


class AddProduct(CreateView):
    form_class=ProductForm
    model=Products
    template_name='addproduct.html'
    success_url=reverse_lazy('Dealer')
    def form_valid(self, form):
        form.instance.user=self.request.user
        self.object=form.save()
        return super().form_valid(form)


class Profile(TemplateView):
    template_name="profile.html"