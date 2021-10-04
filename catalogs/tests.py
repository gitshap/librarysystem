from django.test import TestCase
from catalogs.models import Book


class BookTestcase(TestCase):
    def setUp(self):
        Book.objects.create(title_proper="New Book 1",
                            place_of_publication="New Book 1 Publication")

    def test_book_has_place_of_publication(self):
        """ Book must have a place of publication"""
        new_book = Book.objects.get(title_proper="New Book 1")
        self.assertEqual(new_book.place_of_publication,
                         "New Book 1 Publication")
