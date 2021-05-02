from django.db import models


# Create your models here.

class Category(models.Model):
    title = models.CharField("Title", max_length=50)
    deleted = models.BooleanField(default=False)


class Movie(models.Model):
    title = models.CharField("Title", max_length=50)
    description = models.CharField("Descirption", max_length=150)
    categories = models.ManyToManyField(Category, related_name="movies")
    year = models.IntegerField("Year", null=True, blank=True)
    image = models.ImageField("Image", blank=True)
    deleted = models.BooleanField(default=False)
