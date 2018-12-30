from django.shortcuts import render
from django.views.generic import TemplateView


class EcommerceHomeView(TemplateView):
    template_name = 'e_commerce/index.html'
