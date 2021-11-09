from django.urls import path

from catalogs.views import create_book, view_book, update_book, delete_book

app_name = 'catalogs'
urlpatterns = [
    path('book/create-book', create_book, name='create-book'),
    path('book/update_book/<str:title_proper>',
         update_book, name='update_book'),
    path('book/view_book/<str:title_proper>', view_book, name='view_book'),
    path('book/delete_book/<str:title_proper>', delete_book, name='delete_book')

]
