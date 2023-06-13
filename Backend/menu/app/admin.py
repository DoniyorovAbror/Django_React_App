from django.contrib import admin
from .models import *

# Register your models here.

class FoodAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}
    list_display = ('name', 'get_description')
    list_filter = ['category']
    def get_description(self, obj):
        get_description = obj.description[0: 80]
        return get_description
    get_description.short_description = 'Description'


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Food, FoodAdmin)
admin.site.register(Category, CategoryAdmin)