from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'product_type', 'stock', 'created_at')
    list_filter = ('product_type', 'category')
    search_fields = ('name', 'description')
    list_editable = ('price', 'stock')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-created_at',)
