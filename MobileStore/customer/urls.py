from django.urls import path
from .views import *

urlpatterns = [
    path("CutHomw/",CustHome.as_view(),name='Customer')
]
