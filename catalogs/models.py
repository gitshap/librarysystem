from django.db import models

from core.models import TimeStampedModel

# Book Models
""" Title Proper Model """


class TitleProper(TimeStampedModel):
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


""" Publication Model """


class Publication(TimeStampedModel):
    place_of_publication = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    date_of_publication = models.DateField()

    def __str__(self):
        return self.publisher
