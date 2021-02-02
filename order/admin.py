from django.contrib import admin

from order.models import Order, Counter, OrderUnit

admin.site.register(Order)
admin.site.register(OrderUnit)
admin.site.register(Counter)