from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from blog.models import BlogPost


class BlogPostSitemap(Sitemap):

    def items(self):
        return BlogPost.objects.all()


class PortfolioSitemap(Sitemap):

    def items(self):
        return ['portfolio']

    def location(self, item):
        return reverse(item)





