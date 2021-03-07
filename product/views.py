from rest_framework import generics

from product.models import Product, ProductCategory
from product.serializers import ProductCategorySerializer, ProductReadSerializer, \
    ProductWriteSerializer


class ProductListCreate(generics.ListCreateAPIView):
    queryset = Product.objects.filter(deleted=False)
    # serializer_class = ProductSerializer
    read_serializer = ProductReadSerializer
    write_serializer = ProductWriteSerializer

    def get_serializer_class(self):

        if self.request.method == 'GET':
            return self.read_serializer
        else:
            return self.write_serializer


class ProductRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    read_serializer = ProductReadSerializer
    write_serializer = ProductWriteSerializer

    def get_serializer_class(self):

        if self.request.method == 'GET':
            return self.read_serializer
        else:
            return self.write_serializer

    def perform_destroy(self, instance):
        instance.deleted = True
        instance.save()


class CategoryList(generics.ListAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
