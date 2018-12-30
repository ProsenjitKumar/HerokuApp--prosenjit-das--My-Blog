from django.conf.urls import re_path
from . import views


urlpatterns = [
    re_path('cart/', views.cart, name='cart'),
]