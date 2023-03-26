from django.db import models
from account.models import CustUser
from store.models import Products

# Create your models here.
class Cart(models.Model):
    mobile=models.ForeignKey(Products,on_delete=models.CASCADE,related_name='M_cart',null=True)
    user=models.ForeignKey(CustUser,on_delete=models.CASCADE,related_name='U_cart')
    options=(
        ("carted","carted"),
        ("purchased","purchased")
    )
    status=models.CharField(max_length=100,choices=options,default="carted")

class Review(models.Model):
    comment=models.CharField(max_length=200)
    datetime=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(CustUser,on_delete=models.CASCADE,related_name='commented_user')
    product=models.ForeignKey(Products,on_delete=models.CASCADE,related_name='commented_product')

class Purchase(models.Model):
    city=models.CharField(max_length=100,null=True)
    post=models.CharField(max_length=100,null=True)
    pin=models.IntegerField(null=True)
    quantity=models.IntegerField(null=True)
    options=(
        ("carted","carted"),
        ("purchased","purchased")
    )
    status=models.CharField(max_length=100,choices=options,default="purchased")
    mobile=models.ForeignKey(Products,on_delete=models.CASCADE,related_name='m_purchase',null=True)
    user=models.ForeignKey(CustUser,on_delete=models.CASCADE,related_name='u_purchase')