from django.shortcuts import render
from catalogs.models import Book
from catalogs.forms import TitleProperForm, PublicationForm


def create_book(request):
    title_proper_form = TitleProperForm()
    publication_form = PublicationForm()
