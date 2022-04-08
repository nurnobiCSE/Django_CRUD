from turtle import title
from django.db import models

# Create your models here.
class BookList(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    author = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.title
