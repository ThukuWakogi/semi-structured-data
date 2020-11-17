from django.db import models
from django.contrib.auth import get_user_model


# Naive Model
class Book(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField(help_text='in cents')
    weight = models.PositiveIntegerField(help_text='in grams')

    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.OneToOneField(get_user_model(), primary_key=True, on_delete=models.CASCADE)
    books = models.ManyToManyField(Book)
