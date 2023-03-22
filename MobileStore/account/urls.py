from django.urls import path
from .views import *

urlpatterns = [
    path("Reg/",Reg.as_view(),name='Reg'),
    path("logout/",LogOut.as_view(),name='logout'),
    
]
