from django.contrib import admin

from .models import Profile, JobTitle


@admin.register(Profile)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('user', 'company', 'title')
    ordering = ('user', 'company','title')


@admin.register(JobTitle)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    ordering = ('name',)
