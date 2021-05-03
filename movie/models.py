from django.db import models


# Create your models here.

class Category(models.Model):
    title = models.CharField("Title", max_length=50)
    deleted = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        db_table = "itw_category"


class Movie(models.Model):
    title = models.CharField("Title", max_length=50)
    producent = models.CharField("Producent", max_length=30)
    description = models.CharField("Descirption", max_length=150)
    categories = models.ManyToManyField(Category, related_name="movies")
    year = models.IntegerField("Year", null=True, blank=True)
    image = models.ImageField("Image", blank=True)
    deleted = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Movie"
        verbose_name_plural = "Movies"
        db_table = "itw_movie"

    def get_categories(self):
        return self.categories.all()


class Serial(models.Model):
    title = models.CharField("Title", max_length=50)
    description = models.CharField("Descirption", max_length=150, blank=True)
    categories = models.ManyToManyField(Category, related_name="categories")
    year = models.IntegerField("Year", null=True, blank=True)
    season_no = models.IntegerField("Number of seasons")
    deleted = models.BooleanField(default=False)


class Season(models.Model):
    title = models.CharField("Title", max_length=50)
    description = models.CharField("Descirption", max_length=150, blank=True)
    episode_no = models.IntegerField("Number of epiosdes")
    serial = models.ForeignKey(Serial, on_delete=models.CASCADE, related_name="seasons")
    deleted = models.BooleanField(default=False)


class Episode(models.Model):
    title = models.CharField("Title", max_length=50)
    description = models.CharField("Descirption", max_length=150, blank=True)
    season = models.ForeignKey(Season, on_delete=models.CASCADE, related_name="episodes")
    deleted = models.BooleanField(default=False)
