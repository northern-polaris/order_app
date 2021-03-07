from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from product.models import Product, ProductCategory


class ProductReadSerializer(serializers.ModelSerializer):
    # product_category = SerializerMethodField()
    product_category_name = SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'default_price', 'description', 'product_category', 'product_category_name']

    # def get_product_category(self, obj):
    #     return list(obj.product_category.all().values_list('name', flat=True))

    def get_product_category_name(self, obj):
        return list(obj.product_category.all().values_list('name', flat=True))


class ProductWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'default_price', 'description', 'product_category']


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ['id', 'name']
