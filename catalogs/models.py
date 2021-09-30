from django.db import models

class Book(models.Model):
    isbn = models.CharField(max_length=11)
