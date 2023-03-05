from django.db import models

# Create your models here.

class Booksdata(models.Model):
    title = models.CharField(max_length=210)
    authors = models.CharField(max_length=540)
    average_rating = models.DecimalField(max_digits=3,decimal_places=2)
    language_code = models.CharField(max_length=5)
    num_pages = models.IntegerField()
    ratings_count = models.IntegerField()
    text_reviews_count = models.IntegerField()
    publication_date = models.CharField(max_length=10)
    publisher = models.CharField(max_length=60)
    bookshelf_number = models.CharField(max_length=2)
    level = models.PositiveSmallIntegerField()
    available = models.BooleanField(default=1)