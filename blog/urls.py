from django.conf.urls import re_path
from blog.views import *

app_name = 'blog'


urlpatterns = [
    re_path('^$', BlogHomeView.as_view(), name='home_blog'),
    re_path('(?P<slug>[-\w]+)/$', BlogDetailView.as_view(), name='blog_details'),
]


