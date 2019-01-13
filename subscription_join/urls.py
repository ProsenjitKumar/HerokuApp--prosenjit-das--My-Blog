from django.conf.urls import re_path
from .views import *

urlpatterns = [
    re_path('contact/', ContactView.as_view(), name='contact'),
    re_path('success/', Success.as_view(), name='success'),
    re_path('join-me/', JoinFormView.as_view(), name='join'),
]
