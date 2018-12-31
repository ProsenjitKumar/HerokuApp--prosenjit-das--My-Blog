from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import BlogPost


class BlogHomeView(ListView):
    model = BlogPost
    paginate_by = 15
    template_name = 'blog/index.html'


class BlogDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/single-post-1.html'



