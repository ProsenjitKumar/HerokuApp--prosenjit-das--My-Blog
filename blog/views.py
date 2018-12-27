from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView
from .models import BlogPost


class BlogHomeView(ListView):
    model = BlogPost
    template_name = 'blog/index.html'


class BlogDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/single-post-1.html'



