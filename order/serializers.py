from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from order.models import Order, OrderUnit, Counter


class OrderUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderUnit
        fields = ["product_id", "amount", "price"]


class OrderSerializer(serializers.ModelSerializer):
    order_units = OrderUnitSerializer(many=True)
    date_registered = SerializerMethodField()
    customer_name = SerializerMethodField(read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'customer_id', 'order_units', 'code', 'date_registered', 'code_year', 'creator_id',
                  'customer_name']
        read_only_fields = ('code', 'id', 'date_registered', 'code_year', 'creator_id')

    def get_customer_name(self, obj):
        customer = obj.customer_id
        return f'{customer.full_name()}'

    def get_date_registered(self, obj):
        return obj.date_registered.strftime('%m/%d/%Y')

    def create(self, validated_data):
        logged_user = self._kwargs['context']['request'].user
        order_units = validated_data.pop('order_units')
        validated_data['creator_id'] = logged_user
        order = super().create(validated_data)

        for order_unit in order_units:
            order_unit['order_id'] = order
            OrderUnit.objects.create(**order_unit)

        return order

    def update(self, instance, validated_data):

        logged_user = self._kwargs['context']['request'].user
        order_units = validated_data.pop('order_units')
        validated_data['creator_id'] = logged_user
        order = super().update(instance, validated_data)

        instance.order_units.all().delete()

        for order_unit in order_units:
            order_unit['order_id'] = order
            OrderUnit.objects.create(**order_unit)

        return order
