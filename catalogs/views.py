from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from catalogs.models import Book
from catalogs.forms import BookForm


def create_book(request):

    # check if user is creating a new post
    if request.method == "POST":
        book_form = BookForm(request.POST)

        if book_form.is_valid():
            book_form.save()
            return HttpResponse("Thanks")

    else:
        book_form = BookForm()  # otherwise create a new blank form

    context = {
        "book_form": book_form,
    }
    return render(request, "partials/create_book.html", context=context)
