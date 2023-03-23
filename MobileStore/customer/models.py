from django.db import models
from account.models import CustUser
from store.models import Products

# Create your models here.
class Cart(models.Model):
    mobile=models.ForeignKey(Products,on_delete=models.CASCADE,related_name='M_cart',null=True)
    user=models.ForeignKey(CustUser,on_delete=models.CASCADE,related_name='U_cart')

class Review(models.Model):
    comment=models.CharField(max_length=200)
    datetime=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(CustUser,on_delete=models.CASCADE,related_name='commented_user')
    product=models.ForeignKey(Products,on_delete=models.CASCADE,related_name='commented_product')
