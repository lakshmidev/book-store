# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

from autoslug import AutoSlugField



class Category(models.Model):
    """Stores the list of Book Categories"""
    name = models.CharField(max_length=255, help_text="Enter Book Category Name")
    slug = AutoSlugField(
                max_length=255, unique=True,
                populate_from='name',
                help_text=_("The hyphenated category name in all lowercase and unique")
            )
    
    class Meta:
        ordering = ['id']
    
    def __unicode__(self):
        return "Category Name: %s" % (self.name)


class SubCategory(models.Model):
    """Store Subcategories of the book for each category"""
    category = models.ForeignKey(Category)
    subcategory_name = models.CharField(max_length = 255, help_text="Enter SubCategory Name")
    slug = AutoSlugField(
                max_length=255, unique=True,
                populate_from='subcategory_name',
                help_text=_("The hyphenated Subcategory name in all lowercase and unique")
            )
    
    class Meta:
        ordering = ['id']
    
    def __unicode__(self):
        return self.subcategory_name


class Book(models.Model):
    """Stores Book Details"""
    subcategory = models.ForeignKey(SubCategory)
    title = models.CharField(max_length=500, help_text="Enter Book Title")
    description = models.TextField(help_text="Enter Book Description")
    cover_photo = models.ImageField(null=True, blank=True)
    author = models.CharField(max_length=255)
    published = models.BooleanField(default=True)
    published_by = models.CharField(max_length=255, help_text="Enter Book publisher name", null=True, blank=True)
    published_at = models.DateTimeField(help_text="Enter Book Published Date", null=True, blank=True)
    price = models.IntegerField(help_text="Enter Book Price")
    discount = models.IntegerField(default=0, help_text="Enter Discount Value")
    count = models.IntegerField(help_text="Enter count of book")
    is_in_stock = models.BooleanField(default=True)
    delievery_charge = models.IntegerField(default=0, help_text="Enter delievery charge value if applicable")
    
    def __unicode__(self):
        return self.title

