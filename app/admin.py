from django.contrib import admin
from .models import ProductType, Product, Feedback

@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ['title']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'type', 'price']
    list_filter = ['type']
    search_fields = ['title']

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['author_full_name', 'author_tg', 'estimation', 'date']
    list_filter = ['content', 'date']
    search_fields = ['author_tg', 'date']
