from django.db import models

from core.models import TimeStampedModel

# Book Models


class Book(TimeStampedModel):

    # placeholder choices 1
    CHOICE_1 = 'Choice 1'
    CHOICE_2 = 'Choice 2'
    CHOICE_3 = 'Choice 3'
    # placeholder choices 2
    THE_CHOICES = [
        (CHOICE_1, 'Choice 1'),
        (CHOICE_2, 'Choice 2'),
        (CHOICE_3, 'Choice 3'),
    ]


    # title proper model
    title_proper = models.CharField(max_length=255)
    responsibility = models.CharField(max_length=255)
    preferred_title = models.CharField(max_length=255)
    parallel_title = models.CharField(max_length=255)
    main_creator = models.CharField(max_length=255)
    added_entry_creator = models.CharField(max_length=255)
    contributors = models.CharField(max_length=255)
    added_entry_corporate = models.CharField(max_length=255)

    # publication model
    place_of_publication = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    # date_of_publication = models.DateField()
    edition = models.CharField(max_length=255)
    extent_of_text = models.CharField(max_length=255)
    dimension = models.CharField(max_length=10)
    series = models.CharField(max_length=10)
    supplementary_content = models.CharField(max_length=10, choices=THE_CHOICES, default=CHOICE_1)
    content_type = models.CharField(max_length=10, choices=THE_CHOICES, default=CHOICE_1)
    media_type = models.CharField(max_length=10, choices=THE_CHOICES, default=CHOICE_1)
    carrier_type = models.CharField(max_length=10, choices=THE_CHOICES, default=CHOICE_1)
    identifier_isbn = models.CharField(max_length=11)
    url = models.CharField(max_length=255)

    # access point model


    # local information model
    call_number = models.CharField(max_length=10, choices=THE_CHOICES, default=CHOICE_2)
    accession = models.CharField(max_length=255)
    language = models.CharField(max_length=10, choices=THE_CHOICES, default=CHOICE_1)
    library_location = models.CharField(max_length=10, choices=THE_CHOICES, default=CHOICE_1)
    # TODO: electronic access
    # TODO: conver image file
    # TODO: entered by
    # TODO: updated by

    

    def __str__(self):
        return f"Book {self.title_proper}"
