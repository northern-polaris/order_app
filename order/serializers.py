from rest_framework import serializers

from order.models import Order, OrderUnit, Counter


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"

    # def create(self, validated_data):
    #     last_counter = Counter.objects.last()
    #
    #     counter = Counter.objects.create(name='ORD', value=last_counter.value + 1)
    #     validated_data['code'] = counter.value
    #
    #     return super().create(validated_data)


class OrderUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderUnit
        fields = "__all__"
