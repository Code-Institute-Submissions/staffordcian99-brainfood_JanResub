from django.contrib import admin
from .models import MenuItem, Category

# Register your models here.

class MenuItemAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'price',
        'image',
    )

    ordering = ('category',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(Category, CategoryAdmin)
