from django.db import models

# Create your models here.
class AuthorModel(models.Model):
    name = models.CharField(max_length=40)
    bio = models.TextField(max_length=200)
    dateOfBirth = models.DateField

def __str__(self):
    return self.name
