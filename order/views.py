from collections import OrderedDict

from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination, BasePagination
from rest_framework.permissions import BasePermission
from rest_framework.response import Response

from agent.models import Customer
from order.models import Order, OrderUnit
from order.serializers import OrderSerializer, OrderUnitSerializer

# class IsShites(BasePermission):
#     """
#     Allows access only to Shites users.
#     """
#
#     def has_permission(self, request, view):
#         groups = request.user.groups
#         if "SHites" in groups:
#             return True
#         return False
from product.models import Product


class OrderListCreate(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    # permissions_classes = (IsShites,)


class OrderRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


# class my(PageNumberPagination):
#
#     def get_paginated_response(self, data):
#         return Response(OrderedDict([
#                 ('count', self.page.paginator.count),
#                 ('next', self.get_next_link()),
#                 ('previous', self.get_previous_link()),
#
#             ('data', data)
#         ]))
#
@api_view(['GET'])
def order_form_dependencies(request):
    data = {
        'customers': [{'id': customer.id, 'name': customer.full_name()} for customer in
                      Customer.objects.filter(deleted=False)],

        'products': [{'id': product.id, 'name': product.name, 'price': product.default_price} for product in
                     Product.objects.filter(deleted=False)],
    }
    return Response(data)
