from django.urls import path

from catalogs.views import create_book

urlpatterns = [
    path('book/create-book', create_book, name='create_book'),
]
