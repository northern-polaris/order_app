from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from agent.models import Customer
from order.models import Order
from order.serializers import OrderSerializer
from product.models import Product


class OrderListCreate(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


@api_view(['GET'])
def order_form_dependencies(request):
    data = {
        'customers': [{'id': customer.id, 'name': customer.full_name()} for customer in
                      Customer.objects.filter(deleted=False)],

        'products': [{'id': product.id, 'name': product.name, 'price': product.default_price} for product in
                     Product.objects.filter(deleted=False)],
    }
    return Response(data)
