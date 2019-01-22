from django.shortcuts import render
from django.views.generic import ListView
from .models import (
    Portfolio,
    Skills,
    Projects,
    CurrentPosition,
    Experience,
    EducationalBackground,
    Gallery,
)


class PortfolioView(ListView):
    context_object_name = 'portfolio_list'
    queryset = Portfolio.objects.all()
    extra_context = {
        'projects_list': Projects.objects.all(),
        'skills_list': Skills.objects.all(),
        'current_position_list': CurrentPosition.objects.all(),
    }
    template_name = 'portfolio/index.html'


class GalleryView(ListView):
    model = Gallery
    template_name = 'portfolio/gallery.html'


