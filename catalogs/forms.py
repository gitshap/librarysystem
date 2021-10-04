from django.db.models.base import Model
from django.forms import ModelForm
from crispy_forms.helper import FormHelper

from catalogs.models import Book


class TitleProperForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(TitleProperForm, self).__init__(*args, **kwargs)
        self.fields['title_proper'].label = ""
        self.fields['responsibility'].label = ""
        self.fields['preferred_title'].label = ""
        self.fields['parallel_title'].label = ""
        self.fields['main_creator'].label = ""
        self.fields['added_entry_creator'].label = ""
        self.fields['contributors'].label = ""
        self.fields['added_entry_corporate'].label = ""

    class Meta:
        model = Book
        fields = ['title_proper', 'responsibility', 'preferred_title', 'parallel_title',
                  'main_creator', 'added_entry_creator', 'contributors', 'added_entry_corporate']


class PublicationForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(PublicationForm, self).__init__(*args, **kwargs)
        self.fields['place_of_publication'].label = ""
        self.fields['publisher'].label = ""

    class Meta:
        model = Book
        fields = ['place_of_publication', 'publisher']
