from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

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


@api_view(['POST'])
def deactivate_seller(request):
    id = request.data["id"]
    is_active = request.data["is_active"]
    seller = User.objects.filter(groups__name='Shites').get(id=id)
    seller.is_active = is_active
    seller.save()
    return Response({"message": "Veprimi u krye me sukses"})
