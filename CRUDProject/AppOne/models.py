from django.db import models

# Create your models here.
class BookModel(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publication_date = models.DateField()

def __str__(self):
    return self.title
