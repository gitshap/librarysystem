from django.db.models.base import Model
from django.forms import ModelForm

from catalogs.models import Book


class TitleProperForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title_proper', 'responsibility', 'preferred_title', 'parallel_title',
                  'main_creator', 'added_entry_creator', 'contributors', 'added_entry_corporate']


class PublicationForm(ModelForm):
    class Meta:
        model = Book
        fields = ['place_of_publication', 'publisher', 'date_of_publication']
