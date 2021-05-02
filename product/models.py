from django.db import models
from django.db.models import Q


class ProductCategory(models.Model):
    name = models.CharField(max_length=50, null=False)

    class Meta:
        verbose_name = "Product Category"
        verbose_name_plural = "Product Categories"
        db_table = "itw_product_category"

    def __str__(self):
        return '{} '.format(self.name)


class Product(models.Model):
    name = models.CharField(max_length=50, null=True)
    default_price = models.FloatField(null=True)
    description = models.CharField(max_length=50, null=True)
    product_category = models.ManyToManyField(to=ProductCategory)
    deleted = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        db_table = "itw_product"

    def __str__(self):
        return '{} '.format(self.id)
