from django.contrib.auth.models import User, Group
from rest_framework import serializers

from agent.models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'company_name']


class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']

    def create(self, validated_data):
        seller = super().create(validated_data)
        seller_group = Group.objects.get(name='Shites')
        seller_group.user_set.add(seller)
        return seller
