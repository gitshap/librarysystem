from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from catalogs.models import Book
from catalogs.forms import BookForm
from accounts.views import home_view
from django.contrib import messages
from django.http import HttpResponseRedirect


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


# view specific book
def view_book(request, title_proper):
    book = Book.objects.get(title_proper=title_proper)

    template_name = 'view_book.html'

    context = {
        'book': book
    }

    return render(request, template_name, context=context)


def update_book(request, title_proper):
    book = Book.objects.get(title_proper=title_proper)
    form = BookForm()
    template_name = 'view_book.html'
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid:
            form.save()
            # add a message saying success
            messages.success(request, "Added a new book")
            return redirect(home_view)
        else:
            messages.warning(request, "Please see errors")
    context = {
        'book': book,
        'form': form,
    }
    return render(request, template_name, context=context)


def delete_book(request, title_proper):
    book = Book.objects.get(title_proper=title_proper)
    book.delete()
    messages.success(request, "Book deleted")
    return redirect(home_view)

# TODO: DRY ( Mix everything in into one view )
