from django.db.models.base import Model
from django.forms import ModelForm
from crispy_forms.helper import FormHelper

from catalogs.models import Book


class BookForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        self.fields["title_proper"].label = ""
        self.fields["responsibility"].label = ""
        self.fields["preferred_title"].label = ""
        self.fields["parallel_title"].label = ""
        self.fields["main_creator"].label = ""
        self.fields["added_entry_creator"].label = ""
        self.fields["contributors"].label = ""
        self.fields["added_entry_corporate"].label = ""
        self.fields["place_of_publication"].label = ""
        self.fields["publisher"].label = ""

    class Meta:
        model = Book
        fields = "__all__"
