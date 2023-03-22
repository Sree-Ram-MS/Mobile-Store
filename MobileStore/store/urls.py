from django.urls import path
from .views import *

urlpatterns = [
    path("DealerHome/",DealerHome.as_view(),name='Dealer'),
    path("add/",AddProduct.as_view(),name='AddProduct'),
    path("pro/",Profile.as_view(),name='profile')
]
