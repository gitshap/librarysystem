from django.http.response import HttpResponse
from django.shortcuts import render
from catalogs.models import Book
from catalogs.forms import TitleProperForm, PublicationForm


def create_book(request):
    if request.method == 'POST':
        title_proper_form = TitleProperForm(request.POST)
        publication_form = PublicationForm(request.POST)

        if title_proper_form.is_valid() and publication_form.is_valid():
            book = title_proper_form.save(commit=False)

            place_of_publication = request.POST.get('place_of_publication')
            publisher = request.POST.get('publisher')

            book.place_of_publication = place_of_publication
            book.publisher = publisher

            book.save()
            return HttpResponse(book)
    else:
        title_proper_form = TitleProperForm()
        publication_form = PublicationForm()

    context = {
        'title_proper_form': title_proper_form,
        'publication_form': publication_form,
    }
    return render(request, 'partials/create_book.html', context=context)
