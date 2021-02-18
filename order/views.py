from collections import OrderedDict

from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.pagination import PageNumberPagination, BasePagination
from rest_framework.permissions import BasePermission
from rest_framework.response import Response

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
