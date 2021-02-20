from django.contrib.auth.models import User
from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    company_name = models.CharField(max_length=50)
    deleted = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"
        db_table = "itw_customer"

    def __str__(self):
        return 'Klient {} '.format(self.id)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
