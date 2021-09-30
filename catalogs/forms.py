from django.db.models.base import Model
from django.forms import ModelForm
from catalogs.models import TitleProper, Publication


class TitleProperForm(ModelForm):
    class Meta:
        model = TitleProper
        fields = '__all__'


class PublicationForm(ModelForm):
    class Meta:
        model = Publication
        fields = '__all__'