from django.urls import path
from .views import *

urlpatterns = [
    path("DealerHome/",DealerHome.as_view(),name='Dealer'),
    path("add/",AddProduct.as_view(),name='AddProduct'),
    path("mypro/",MyProduct.as_view(),name='MyPro'),
    path("pro/",Profile.as_view(),name='profile'),
    path('updatepro/<int:pk>/',UpdateProduct.as_view(),name='Update'),
    path('deletepro/<int:pk>/',RemoveProduct.as_view(),name='Remove'),
]
