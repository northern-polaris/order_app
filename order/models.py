from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from agent.models import Customer
from product.models import Product


class Order(models.Model):
    code = models.IntegerField()
    code_year = models.IntegerField()
    date_registered = models.DateTimeField(auto_now=True)
    customer_id = models.ForeignKey(to=Customer, related_name="orders", on_delete=models.CASCADE)
    creator_id = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="orders")

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"
        db_table = "itw_order"


class OrderUnit(models.Model):
    order_id = models.ForeignKey(to=Order, on_delete=models.CASCADE)
    product_id = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    amount = models.IntegerField()
    price = models.IntegerField()

    class Meta:
        verbose_name = "OrderUnit"
        verbose_name_plural = "OrderUnites"
        db_table = "itw_order_units"


class Counter(models.Model):
    name = models.CharField(max_length=10)
    value = models.IntegerField()

    class Meta:
        verbose_name = "Counter"
        verbose_name_plural = "Counters"
        db_table = "itw_counter"
