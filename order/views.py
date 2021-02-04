from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.permissions import BasePermission

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


class OrderUnitListCreate(generics.ListCreateAPIView):
    queryset = OrderUnit.objects.all()
    serializer_class = OrderUnitSerializer


class OrderUnitRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderUnit.objects.all()
    serializer_class = OrderUnitSerializer
