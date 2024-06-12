from django.contrib import admin
from .models import ProductType, ProductTypeImage, Product, Feedback

@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ['title']

@admin.register(ProductTypeImage)
class ProductTypeAdmin(admin.ModelAdmin):
    list_filter = ['product_type']
    search_fields = ['product_type']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'type', 'price']
    list_filter = ['type']
    search_fields = ['title']

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['author_full_name', 'author_tg', 'estimation', 'date']
    list_filter = ['author_tg', 'date']
    search_fields = ['author_tg', 'date']
