# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from book_store.models import Category, SubCategory, Book

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('category', 'subcategory_name')
    list_filter = ('category__name',)
    search_fields =('category__name',)


class BookAdmin(admin.ModelAdmin):
    list_display = ('subcategory','title', 'author', 
        'published_by', 'published_at', 'published', 'price', 
        'discount', 'count', 'is_in_stock', 'delievery_charge', )
    list_filter = ('subcategory__subcategory_name','title', 'author', 
        'published_by','published', 'price', )
    search_fields = ('subcategory__subcategory_name','title', 'author',)



admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Book,BookAdmin)
