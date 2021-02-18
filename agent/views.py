from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import generics

from agent.models import Customer
from agent.serializers import CustomerSerializer, SellerSerializer


class CustomerListCreate(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class SellerListCreate(generics.ListCreateAPIView):
    queryset = User.objects.filter(groups__name='Shites')
    serializer_class = SellerSerializer


class SellerRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.filter(groups__name='Shites')
    serializer_class = SellerSerializer
