from django.contrib import admin
from .models import Company


@admin.register(Company)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'short_name', 'ogrn', 'grn', 'status')
    list_filter = ('full_name', 'short_name', 'ogrn', 'grn',)
    search_fields = ('full_name', 'short_name', 'ogrn', 'grn',)
    #prepopulated_fields = {'url': ('full_name',)}
    #raw_id_fields = ('author',)
    date_hierarchy = 'created'
    ordering = ('status', 'created')