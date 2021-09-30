from django.shortcuts import render
from catalogs.models import TitleProper, Publication
from catalogs.forms import (
    TitleProperForm, PublicationForm
)


def create_title_proper_form(request):
    form = TitleProperForm()
    context = {
        "form": form
    }
    return render(request, "partials/title_proper_form.html", context=context)

def create_publication_form(request):
    form = PublicationForm()
    context = {
        "form": form
    }
    return render(request, "partials/publication_form.html", context=context)
