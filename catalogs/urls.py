from django.urls import path

from catalogs.views import create_title_proper_form, create_publication_form, create_title_proper

urlpatterns = [
    path('htmx/create-title-proper/',
         create_title_proper, name='create_title_proper'),
    path('htmx/create-title-proper-form/',
         create_title_proper_form, name='create_title_proper_form'),
]
