from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.contrib.auth.views import PasswordChangeView
from account.models import CustUser
from store.models import Products
from .models import Cart
from django.urls import reverse_lazy

# Create your views here.
# Home page for customer
class CustHome(TemplateView):
    template_name="userpage.html"
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["products"]=Products.objects.all()
        return context
    

class CProfile(TemplateView):
    template_name="cprofile.html"

# My cart section

class MyCart(TemplateView):
    template_name='mycart.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["products"]=Cart.objects.filter(user=self.request.user)
        return context
    
def addcart(request,*args,**kwargs):
    id=kwargs.get("pid")
    mobile=Products.objects.get(id=id)
    user=request.user
    Cart.objects.create(mobile=mobile,user=user)
    return redirect('Customer')

def delcart(request,*args,**kwargs):
    id=kwargs.get("pid")
    user=request.user
    Cart.objects.filter(id=id).delete()
    return redirect('MyCart')

class Puchase(TemplateView):
    template_name="purchase.html"
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["order"]=Cart.objects.filter(user=self.request.user)
        return context
    

#  change password

class ChangePassword(PasswordChangeView):
    template_name = 'cchangepass.html'
    success_url = reverse_lazy('Customer')    


class BuyNow(TemplateView):
    template_name="buynow.html"
    def get_context_data(self, **kwargs):
        id=kwargs.get('pid')
        context=super().get_context_data(**kwargs)
        context["buy"]=Products.objects.get(id=id)
        return context
    

