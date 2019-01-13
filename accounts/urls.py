from django.conf.urls import re_path
from .views import RegistrationView


urlpatterns = [
    re_path('registration/', RegistrationView.as_view(), name='registration'),
]