from rest_framework import serializers

from order.models import Order, OrderUnit, Counter


class OrderUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderUnit
        fields = ["product_id", "amount"]


class OrderSerializer(serializers.ModelSerializer):
    order_units = OrderUnitSerializer(many=True)

    class Meta:
        model = Order
        fields = ['code', 'code_year', 'customer_id', 'creator_id', 'order_units']
