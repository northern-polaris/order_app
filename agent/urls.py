from django.urls import path

from agent.views import CustomerListCreate, SellerListCreate, SellerRetrieveUpdateDestroy

urlpatterns = [
    path('customer/', CustomerListCreate.as_view()),
    path('seller/', SellerListCreate.as_view()),
    path('seller/<int:pk>/', SellerRetrieveUpdateDestroy.as_view()),
]
