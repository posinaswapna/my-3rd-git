from django.urls import path
from app2.views import *
app_name='something!'
urlpatterns=[
    path('swapna/',swapna,name='swapna'),
    path('pavan/',pavan,name='pavan'),
]