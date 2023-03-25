from django.urls import path
from .views import *

urlpatterns = [
    path("CustHome/",CustHome.as_view(),name='Customer'),
    path('mycart/',MyCart.as_view(),name='MyCart'),
    path("pro/",CProfile.as_view(),name='cprofile'),
    path('addcart/<int:pid>',addcart,name='AddCart'),
    path('delcart/<int:pid>',delcart,name='DelCart'),
    path('purchase/',Puchase.as_view(),name='Purchase'),

    path('Buy/<int:pid>',BuyNow.as_view(),name='Buy'),


    path('change/',ChangePassword.as_view(),name='Cpass'),
]
