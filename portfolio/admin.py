from django.contrib import admin
from .models import (
    Portfolio,
    Skills,
    Projects,
    CurrentPosition,
    Experience,
    EducationalBackground,
    Gallery,
)


class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['name', 'updated']
    search_fields = ['name']


admin.site.register(Portfolio, PortfolioAdmin)


class SkillsAdmin(admin.ModelAdmin):
    list_display = ['name', 'percentage', 'updated']
    search_fields = ['name']


admin.site.register(Skills, SkillsAdmin)


class ProjectsAdmin(admin.ModelAdmin):
    list_display = ['name', 'website', 'updated']
    search_fields = ['name']


admin.site.register(Projects, ProjectsAdmin)


class CurrentPositionAdmin(admin.ModelAdmin):
    list_display = ['name', 'website', 'updated']
    search_fields = ['name']


admin.site.register(CurrentPosition, CurrentPositionAdmin)


class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['name', 'website', 'updated']
    search_fields = ['name']


admin.site.register(Experience, ExperienceAdmin)


class EducationalBackgroundAdmin(admin.ModelAdmin):
    list_display = ['degree', 'subject', 'year', 'result', 'updated']
    search_fields = ['name']


admin.site.register(EducationalBackground, EducationalBackgroundAdmin)


class GalleryAdmin(admin.ModelAdmin):
    list_display = ['name', 'image']
    search_fields = ['name']
    prepopulated_fields = {'slug':('name',)}


admin.site.register(Gallery, GalleryAdmin)
