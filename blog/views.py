from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import BlogPost, QuestionPost
from django.utils import timezone


# *************** simple blog start ************************
class BlogHomeView(ListView):
    model = BlogPost
    paginate_by = 9
    ordering = ['-post_date']
    template_name = 'blog/blog-post-list.html'


class BlogDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/blog-single-post.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
# *************** simple blog end ************************


# *************** question blog start ************************
class QuestionPostView(ListView):
    model = QuestionPost
    paginate_by = 9
    ordering = ['-post_date']
    template_name = 'blog/question-post-list.html'


class QuestionDetailView(DetailView):
    model = QuestionPost
    template_name = 'blog/question-single-post.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
# *************** question blog end ************************



