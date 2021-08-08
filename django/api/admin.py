from django.contrib import admin
from api.models import Category, Offer


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_per_page = 25
    list_display_links = ('name', )


@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'category', 'created_at')
    list_per_page = 25
    list_display_links = ('title', )
    ordering = ('created_at', )
