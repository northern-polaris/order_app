from django.urls import path

from agent.views import CustomerListCreate, SellerListCreate

urlpatterns = [
    path('customer/', CustomerListCreate.as_view()),
    path('seller/', SellerListCreate.as_view()),
]
