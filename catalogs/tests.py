from django.test import TestCase
from catalogs.models import Book
from django.shortcuts import get_object_or_404


class BookTestcase(TestCase):
    def setUp(self):
        Book.objects.create(
            title_proper="New Book 1", place_of_publication="New Book 1 Publication"
        )

    def test_book_has_place_of_publication(self):
        """Book must have a place of publication"""
        new_book = Book.objects.get(title_proper="New Book 1")
        self.assertEqual(new_book.place_of_publication, "New Book 1 Publication")

    def test_book_has_same_id_with_publisher(self):
        new_book = Book.objects.get(title_proper="New Book 1")
        book_with_publisher = Book.objects.get(
            place_of_publication="New Book 1 Publication"
        )
        self.assertEqual(new_book.id, book_with_publisher.id)

    def test_book_is_created(self):
        self.assertEqual(True, Book.objects.filter(title_proper="New Book 1").exists())

    def test_if_book_has_created_and_updated(self):
        new_book = Book.objects.get(title_proper="New Book 1")
        created = new_book.created
        modified = new_book.modified
        self.assertIsNotNone(created)
        self.assertIsNotNone(modified)
