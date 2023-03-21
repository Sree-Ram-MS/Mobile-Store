from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView,CreateView,FormView
from .forms import RegForm,LogForm
from .models import CustUser
from django.contrib.auth import authenticate,login
from django.contrib import messages

# Create your views here.
# class Homepage(TemplateView):
#     template_name="Homepage.html"

class Reg(CreateView):
    template_name="Reg.html"
    form_class=RegForm
    model=CustUser
    success_url=reverse_lazy("Homepage")

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
                if ut=="Store":
                    return redirect('store')
                else:
                    login(req,user)
                    return redirect("Customer")
            else:
                return render(req,'Homepage.html',{"form":form_data})
        else:
            return render(req,'Homepage.html',{"form":form_data})