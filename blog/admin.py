from django.contrib import admin
from .models import BlogPost, BlogCategory, QuestionPost


class BlogCategoryAdmin(admin.ModelAdmin):
    list_display_links = ['title']
    list_filter = ['title']
    list_display = ['title']
    list_per_page = 15


admin.site.register(BlogCategory, BlogCategoryAdmin)


class BlogPostAdmin(admin.ModelAdmin):
    list_display_links = ['title']
    list_filter = ['title']
    list_display = ['title']
    list_per_page = 15


admin.site.register(BlogPost, BlogPostAdmin)


class QuestionPostAdmin(admin.ModelAdmin):
    list_display_links = ['title']
    list_filter = ['title']
    list_display = ['title']
    list_per_page = 15


admin.site.register(QuestionPost, QuestionPostAdmin)
