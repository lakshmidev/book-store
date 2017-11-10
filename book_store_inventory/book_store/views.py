# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from book_store.models import Category, SubCategory, Book
from book_store.utils import get_categories


@login_required
def list_books(request, *args, **kwargs):
    """ Used for disblaying all the books.
        if selected particular category, then it will display books
        of thatcategory
    """
    category_list, subcategory_dict = get_categories()
    context_data = {}
    context_data['category_list'] = category_list
    context_data['subcategory_dict'] = subcategory_dict
    book_list = []
    if kwargs.get('subcategory_id'):
        sub_id = kwargs.get('subcategory_id')
        book_list = Book.objects.filter(subcategory__id=sub_id)
    else:
        book_list = Book.objects.all()    
    context_data['book_list'] = book_list
    return render(request, 'book_store/book_list.html', context=context_data)

@login_required
def book_detail(request, *args, **kwargs):
    """ Used for displaying details of the particular book.
    """
    category_list, subcategory_dict = get_categories()
    context_data = {}
    context_data['category_list'] = category_list
    context_data['subcategory_dict'] = subcategory_dict 
    book_list = []
    sub_id = kwargs.get('subcategory_id')
    book_id = kwargs.get('book_id')
    book = None
    if sub_id and book_id:
        try:
            book = Book.objects.get(subcategory__id=sub_id, pk=book_id)
        except:
            pass    
    context_data['book'] = book 
    return render(request, 'book_store/book_details.html', context=context_data)

@login_required
def buy_book(request, *args, **kwargs):
    """ GET: Used to display book overview with quatity field for processing
        payment. 
        POST: Used for getting book price, quatity value to calculaate total price.
            And redirect the user to the payment page with total price.
        request.session: Used for storing invoice/subscription details upon successful
        completion of payment. 
    """
    category_list, subcategory_dict = get_categories()
    context_data = {}
    context_data['category_list'] = category_list
    context_data['subcategory_dict'] = subcategory_dict
    book_list = []
    sub_id = kwargs.get('subcategory_id')
    book_id = kwargs.get('book_id')
    book = None
    if request.method == "POST":
        quantity = request.POST.get('quantity')
        book_price = request.POST.get('book_price')
        total_price = int(quantity)*int(book_price)
        request.session['user_id'] = request.user.id
        request.session['book_id'] = book_id
        request.session['subcategory_id'] = sub_id
        request.session['total_price'] = total_price
        # return redirect("/view-for-processing-payment/")
    if sub_id and book_id:
        try:
            book = Book.objects.get(subcategory__id=sub_id, pk=book_id)
        except:
            pass
    context_data['book'] = book
    return render(request, 'book_store/buy_book.html', context=context_data)


    


