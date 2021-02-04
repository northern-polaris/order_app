from django.shortcuts import render
from rest_framework import generics

from agent.models import Customer
from agent.serializers import CustomerSerializer


class CustomerListCreate(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
