from django.db import models

# Create your models here.

class Borrowed_bookdata(models.Model):
    student_id = models.IntegerField()
    book_id = models.IntegerField()