from rest_framework import serializers

from order.models import Order, OrderUnit, Counter


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['code', 'code_year', 'customer_id', 'creator_id']


class OrderUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderUnit
        fields = "__all__"
