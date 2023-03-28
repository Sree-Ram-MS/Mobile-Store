from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.contrib.auth.views import PasswordChangeView
from account.models import CustUser
from store.models import Products
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.decorators import method_decorator


#==== Decorator ====#
def signin_required(fn):
    def wrapper(req,*args,**kwargs):
        if req.user.is_authenticated:
            return fn(req,*args,**kwargs)
        else:
            return redirect ("Homepage")
    return wrapper


# Create your views here.
# Home page for customer
@method_decorator(signin_required,name='dispatch')
class CustHome(TemplateView):
    template_name="userpage.html"
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["products"]=Products.objects.all()
        context["cart"]=Cart.objects.filter(status="carted")
        context["form"]=ReviewForm()
        context['review']=Review.objects.all()
        context['pst']=Purchase.objects.filter(user=self.request.user)
        return context
    
@method_decorator(signin_required,name='dispatch')
class CProfile(TemplateView):
    template_name="cprofile.html"

# My cart section
@method_decorator(signin_required,name='dispatch')
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
    if Cart.objects.filter(mobile=mobile,status="carted",user=request.user):
        messages.warning(request,"Alredy Added in Cart")
        return redirect('Customer')
    else:
        Cart.objects.create(mobile=mobile,user=user,status="carted")
        messages.success(request,"Added to Cart")
        return redirect('Customer')

def delcart(request,*args,**kwargs):
    id=kwargs.get("pid")
    user=request.user
    Cart.objects.filter(id=id).delete()
    messages.error(request,"Item Removed form cart")
    return redirect('MyCart')

def addreview(request,*args,**kwargs):
    if request.method=="POST":
        id=kwargs.get('pid')
        product=Products.objects.get(id=id)
        user=request.user
        cmnt=request.POST.get("comment")
        Review.objects.create(product=product,user=user,comment=cmnt)
        return redirect('Customer')

class Puchase(TemplateView):
    template_name="purchase.html"
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["order"]=Purchase.objects.filter(user=self.request.user)
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
        context["form"]=PurchaseForm()
        return context
    

    
def buyitem(request,*args,**kwargs):
    id=kwargs.get("pid")
    mobile=Products.objects.get(id=id)
    user=request.user
    city=request.POST.get('city')
    post=request.POST.get('post')
    pin=request.POST.get('pin')
    quantity=request.POST.get('quantity')
    Purchase.objects.create(city=city,post=post,pin=pin,quantity=quantity,mobile=mobile,user=user)
    messages.success(request,"Order has been placed")
    return redirect('Customer')
