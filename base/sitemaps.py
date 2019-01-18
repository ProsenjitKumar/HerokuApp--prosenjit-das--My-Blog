from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from blog.models import BlogPost, QuestionPost


# Dynamic
class BlogPostSitemap(Sitemap):
    def items(self):
        return BlogPost.objects.all()


class QuestionSiteMap(Sitemap):
    def items(self):
        return QuestionPost.objects.all()


# Static
class PortfolioSitemap(Sitemap):
    def items(self):
        return ['portfolio']

    def location(self, item):
        return reverse(item)


class ContactSitemap(Sitemap):
    def items(self):
        return ['contact']

    def location(self, item):
        return reverse(item)





