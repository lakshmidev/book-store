"""book_store_inventory URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

from book_store.views import list_books, book_detail, buy_book

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^accounts/', include('registration.backends.hmac.urls')),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^$', list_books, name="list_books"),
    url(r'^book/(?P<subcategory_id>\d+)/$', list_books, name="list_books"),
    url(r'^book-detail/(?P<subcategory_id>\d+)/(?P<book_id>\d+)/$', 
        book_detail, name="book_detail"),
    url(r'^buy-book/(?P<subcategory_id>\d+)/(?P<book_id>\d+)/$', 
        buy_book, name="buy_book"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
