from django.contrib import admin

from store.models import Products


class ProductsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'price']
    list_filter = ['title', 'category']
    search_fields = ['title', 'category']
    fields = ['title', 'description', 'category', 'residue', 'price']


admin.site.register(Products, ProductsAdmin)