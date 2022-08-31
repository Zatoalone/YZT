from django.contrib import admin

from .models import Well, StatusWell, PurposeWell, Field, Wellbore, Shape, TypeWellbore


@admin.register(Field)
class FieldAdmin(admin.ModelAdmin):
    list_display = ('name', 'uid',)
    list_filter = ('name', 'uid',)
    search_fields = ('name', 'uid')
    ordering = ('name', 'uid',)


@admin.register(StatusWell)
class StatusWellAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    list_filter = ('name', 'description')
    search_fields = ('name', 'description')
    ordering = ('name', 'description')


@admin.register(PurposeWell)
class PurposeWellAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    list_filter = ('name', 'description')
    search_fields = ('name', 'description')
    ordering = ('name', 'description')


@admin.register(Well)
class WellAdmin(admin.ModelAdmin):
    list_display = ('name', 'uid',)
    list_filter = ('name', 'uid',)
    search_fields = ('name', 'uid')
    ordering = ('name', 'uid',)

@admin.register(Shape)
class ShapeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    list_filter = ('name', 'description')
    search_fields = ('name', 'description')
    ordering = ('name', 'description')


@admin.register(TypeWellbore)
class TypeWellboreAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    list_filter = ('name', 'description')
    search_fields = ('name', 'description')
    ordering = ('name', 'description')


@admin.register(Wellbore)
class WellboreAdmin(admin.ModelAdmin):
    list_display = ('name', 'uid',)
    list_filter = ('name', 'uid',)
    search_fields = ('name', 'uid')
    ordering = ('name', 'uid',)
