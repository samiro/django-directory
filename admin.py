from django.contrib import admin
from . import models


@admin.register(models.City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('slug', 'title')


@admin.register(models.Neighborhood)
class NeighborhoodAdmin(admin.ModelAdmin):
    list_display = ('title', 'city')


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')


@admin.register(models.Business)
class BusinessAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'neighborhood', 'address')
