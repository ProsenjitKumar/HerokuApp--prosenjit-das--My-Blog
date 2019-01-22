from django.shortcuts import render
from django.views.generic import TemplateView, View
from .models import (
    Portfolio,
    Skills,
    Projects,
    CurrentPosition,
    Experience,
    EducationalBackground,
)


class PortfolioView(TemplateView):
    template_name = 'portfolio/index.html'


