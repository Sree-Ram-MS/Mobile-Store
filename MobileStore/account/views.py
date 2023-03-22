from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView,CreateView,FormView,View
from .forms import RegForm,LogForm
from .models import CustUser
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.
# Registration form
class Reg(CreateView):
    template_name="Reg.html"
    form_class=RegForm
    model=CustUser
    success_url=reverse_lazy("Homepage")


# Login and First page
class Homepage(FormView):
    template_name='Homepage.html'
    form_class=LogForm
    def post(self,req,*args,**kwargs):
        form_data=LogForm(data=req.POST)
        if form_data.is_valid():
            un=form_data.cleaned_data.get("username")
            pw=form_data.cleaned_data.get("password")
            ut=form_data.cleaned_data.get("usertype")
            user=authenticate(req,username=un,password=pw,usertype=ut)
            if user:
                login(req,user)
                if req.user.usertype=="Store":
                    return redirect("Dealer")
                else:
                    login(req,user)
                    return redirect("Customer")
            else:
                return render(req,'Homepage.html',{"form":form_data})
        else:
            return render(req,'Homepage.html',{"form":form_data})
        
class LogOut(View):
    def get(self,req):
        logout(req)
        return redirect('Homepage')