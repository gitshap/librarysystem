from django.urls import path

from catalogs.views import create_book

app_name = 'catalogs'
urlpatterns = [
    path('book/create-book', create_book, name='create-book'),
]
