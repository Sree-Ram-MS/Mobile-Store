from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.contrib.auth.views import PasswordChangeView
from account.models import CustUser
from store.models import Products
from .models import *
from .forms import *
from django.urls import reverse_lazy

from django.shortcuts import get_object_or_404

from django.contrib.sessions.backends.db import SessionStore
from .models import Cart

def create_cart(request):
    # Create a new cart object
    cart = Cart.objects.create()

    # Get the current session
    session = SessionStore(request.session.session_key)

    # Store the cart ID in the session
    session['cart_id'] = cart.id
    session.save()
    
def get_cart_id(request):
    # Get the current session
    session = SessionStore(request.session.session_key)

    # Get the cart ID from the session
    cart_id = session.get('cart_id')

    return cart_id



def product_id(request, slug, id):
    product=get_object_or_404(Cart, mobile_id=id, slug=slug) 
    return render(request,'userpage.html',{'pid':pid})

# Create your views here.
# Home page for customer
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

    Cart.objects.create(mobile=mobile,user=user,status="carted")
    return redirect('Customer')

def delcart(request,*args,**kwargs):
    id=kwargs.get("pid")
    user=request.user
    Cart.objects.filter(id=id).delete()
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
    ucart=Cart.objects.get(mobile_id=id)
    ucart.status="purchased"
    ucart.save()
    return redirect('Customer')
