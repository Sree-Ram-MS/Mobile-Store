from django.urls import path
from .views import *

urlpatterns = [
    path("DealerHome/",DealerHome.as_view(),name='Dealer'),
    path("add/",AddProduct.as_view(),name='AddProduct'),
    path("mypro/",MyProduct.as_view(),name='MyPro'),
    path("pro/",Profile.as_view(),name='profile')
]
