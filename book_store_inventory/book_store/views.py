# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def list_books(request):
	return render(request, 'book_store/index.html')