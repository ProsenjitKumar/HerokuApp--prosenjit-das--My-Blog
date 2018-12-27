from django.shortcuts import render
from django.views.generic import TemplateView, View


class PortfolioView(TemplateView):
    template_name = 'portfolio/index.html'


