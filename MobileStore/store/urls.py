from django.urls import path
from .views import *

urlpatterns = [
    path("DealerHome/",DealerHome.as_view(),name='Dealer')
]
