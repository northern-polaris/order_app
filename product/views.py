from django.shortcuts import render
from rest_framework import generics

from product.models import Product, ProductCategory
from product.serializers import ProductSerializer, ProductCategorySerializer


class ProductListCreate(generics.ListCreateAPIView):
    queryset = Product.objects.filter(deleted=False)
    serializer_class = ProductSerializer


class ProductRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_destroy(self, instance):
        instance.deleted = True
        instance.save()


class CategoryList(generics.ListAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
