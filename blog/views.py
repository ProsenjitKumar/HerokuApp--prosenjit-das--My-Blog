from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import BlogPost
from django.utils import timezone



class BlogHomeView(ListView):
    model = BlogPost
    paginate_by = 9
    ordering = ['-post_date']
    template_name = 'blog/index.html'


class BlogDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/single-post-1.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context



