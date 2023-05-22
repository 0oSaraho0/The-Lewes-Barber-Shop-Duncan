from django.contrib import admin

from .models import Product

@admin.register(Product)
class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'price',
        'image',
        'description'
    )
    list_filter = ('product',)
