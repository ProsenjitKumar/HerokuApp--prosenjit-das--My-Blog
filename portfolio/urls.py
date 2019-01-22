from django.conf.urls import re_path
from portfolio.views import *


urlpatterns = [
    re_path('', PortfolioView.as_view(),  name='portfolio'),
]