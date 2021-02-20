from django.urls import path

from agent.views import CustomerListCreate, SellerListCreate, SellerRetrieveUpdateDestroy, \
    CustomerRetrieveUpdateDestroy, deactivate_seller

urlpatterns = [
    path('customer/', CustomerListCreate.as_view()),
    path('customer/<int:pk>/', CustomerRetrieveUpdateDestroy.as_view()),
    path('seller/', SellerListCreate.as_view()),
    path('seller/<int:pk>/', SellerRetrieveUpdateDestroy.as_view()),
    path('seller/deactivate/', deactivate_seller),

]
