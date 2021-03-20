from django.db import models


class BookJournalBase(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField(default=0)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Book(BookJournalBase):
    num_pages = models.IntegerField(default=0)
    genre = models.CharField(max_length=255)


class Journal(BookJournalBase):
    TYPE = (
        ('Bullet', 'Bullet'),
        ('Food', 'Food'),
        ('Travel', 'Travel'),
        ('Sport', 'Sport'),
    )

    type = models.CharField(max_length=255, choices=TYPE, default='Bullet')
    publisher = models.CharField(max_length=255)
