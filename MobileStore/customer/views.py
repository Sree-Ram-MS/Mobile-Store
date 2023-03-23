from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from store.models import Products
from .models import Cart

# Create your views here.
# Home page for customer
class CustHome(TemplateView):
    template_name="userpage.html"
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["products"]=Products.objects.all()
        return context
    
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
    mobile=Products.objects.get(id=id)
    user=request.user
    mobile.delete()
    return redirect('MyCart')