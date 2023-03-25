from django.db import models
from account.models import CustUser

# Create your models here.
class Products(models.Model):
    Mobile_pic=models.ImageField(upload_to="product_image",null=True)
    Name=models.CharField(max_length=100)
    Prize=models.IntegerField()
    RAM=models.IntegerField(null=True)
    ROM=models.IntegerField(null=True)
    Battery=models.IntegerField(null=True)
    Processer=models.CharField(max_length=100,null=True)
    Camera=models.CharField(max_length=100,null=True)
    user=models.ForeignKey(CustUser,on_delete=models.CASCADE,related_name="m_store")
    # quantity = models.PositiveIntegerField(default=0)