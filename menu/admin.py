from django.contrib import admin

from .models import Category, Dish

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'cost', 'updated_at']
    ordering = ['updated_at']

