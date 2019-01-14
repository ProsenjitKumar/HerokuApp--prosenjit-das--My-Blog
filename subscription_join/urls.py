from django.conf.urls import re_path
from .views import *

urlpatterns = [
    re_path('contact/', ContactView.as_view(), name='contact'),
    re_path('success/', Success.as_view(), name='success'),
    # News Letter
    #re_path('', newsletter_signup, name='newsletter_signup'),
    #re_path(r'^unsubscription/', newsletter_unsubscribe, name='unsubscribe'),
]
