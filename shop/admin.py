from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import UsersOrders, SiteUser
from .models import Product, Category, Article
# from django.contrib.auth.models import User

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'parent_category']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['header']
    prepopulated_fields = {'slug': ('header',)}



