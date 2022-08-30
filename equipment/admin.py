from django.contrib import admin

from .models import Equipment


@admin.register(Equipment)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name', 'uid', 'banner')
    list_filter = ('name', 'uid',)
    search_fields = ('name', 'uid', 'description')
    ordering = ('name', 'uid',)
