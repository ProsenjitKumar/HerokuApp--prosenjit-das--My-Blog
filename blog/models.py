from django.contrib.auth.models import User
from django.db import models


class EntryQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)


class Blogcategory(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title


class BlogPost(models.Model):
    title = models.CharField(max_length=255, blank=False)
    category = models.ForeignKey(Blogcategory, on_delete=models.CASCADE)
    description = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='blog_post/', blank=True)
    publish = models.BooleanField(default=True)
    slug = models.SlugField(max_length=200, unique=True)
    objects = EntryQuerySet.as_manager()

    def __str__(self):
        return self.title



