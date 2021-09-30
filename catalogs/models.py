from django.db import models


# Book Model
class TitleProper(models.Model):
    title_proper = models.CharField(max_length=255)
    responsibility = models.CharField(max_length=255)
    preferred_title = models.CharField(max_length=255)
    parallel_title = models.CharField(max_length=255)
    main_creator = models.CharField(max_length=255)
    added_entry_creator = models.CharField(max_length=255)
    contributors = models.CharField(max_length=255)
    added_entry_corporate = models.CharField(max_length=255)

    def __str__(self):
        return self.title_proper

class Publication(models.Model):
    place_of_publication = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    date_of_publication = models.DateField()

    def __str__(self):
        return self.publisher