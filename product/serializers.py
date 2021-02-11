
from rest_framework import serializers

from product.models import Product, ProductCategory


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'default_price', 'description', 'product_category', 'deleted']

