from django.contrib import admin

from .models import Well, StatusWell, PurposeWell, Field


@admin.register(Field)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name', 'uid',)
    list_filter = ('name', 'uid',)
    search_fields = ('name', 'uid')
    ordering = ('name', 'uid',)


@admin.register(StatusWell)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name', )
    search_fields = ('name', )
    ordering = ('name',)


@admin.register(PurposeWell)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name', )
    ordering = ('name',)


@admin.register(Well)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name', 'uid',)
    list_filter = ('name', 'uid',)
    search_fields = ('name', 'uid')
    ordering = ('name', 'uid',)
