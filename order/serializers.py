from django.contrib.auth.models import User
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
        fields = ['id', 'customer_id', 'order_units', 'code', 'date_registered', 'code_year', 'creator_id']
        read_only_fields = ('code', 'id', 'date_registered', 'code_year', 'creator_id')

    def create(self, validated_data):
        # logged_user = self._kwargs['context']['request'].user
        order_units = validated_data.pop('order_units')

        logged_user = User.objects.first()
        code = 1
        code_year = 2021
        validated_data['code'] = code
        validated_data['code_year'] = code_year
        validated_data['creator_id'] = logged_user
        order = super().create(validated_data)

        for order_unit in order_units:
            order_unit['order_id'] = order
            product_price = order_unit['product_id'].default_price
            total_price = product_price * order_unit['amount']
            order_unit['price'] = total_price
            OrderUnit.objects.create(**order_unit)

        return order
