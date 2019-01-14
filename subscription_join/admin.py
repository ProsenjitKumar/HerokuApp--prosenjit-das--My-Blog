from django.contrib import admin
from .models import NewsLetterUser, NewsLetter


class NewsLetterUserAdmin(admin.ModelAdmin):
    list_display = ['email', 'date_added',]


admin.site.register(NewsLetterUser, NewsLetterUserAdmin)


class NewsLetterAdmin(admin.ModelAdmin):
    list_display = ['subject', 'status', 'created', ]
    list_per_page = 10


admin.site.register(NewsLetter, NewsLetterAdmin)