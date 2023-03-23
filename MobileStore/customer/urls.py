from django.urls import path
from .views import *

urlpatterns = [
    path("CustHome/",CustHome.as_view(),name='Customer'),
    path('mycart/',MyCart.as_view(),name='MyCart'),
    path('addcart/<int:pid>',addcart,name='AddCart'),
    path('delcart/<int:pid>',delcart,name='DelCart'),
]
