from django.contrib import admin
from .models import BlogPost, Blogcategory


class BlogCategoryAdmin(admin.ModelAdmin):
    list_display_links = ['title']
    list_filter = ['title']
    list_display = ['title']
    list_per_page = 15


admin.site.register(Blogcategory, BlogCategoryAdmin)


class BlogPostAdmin(admin.ModelAdmin):
    list_display_links = ['title']
    list_filter = ['title']
    list_display = ['title']
    list_per_page = 15


admin.site.register(BlogPost, BlogPostAdmin)
