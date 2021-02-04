from django.urls import path

from order.views import OrderListCreate, OrderRetrieveUpdateDestroy, OrderUnitListCreate, OrderUnitRetrieveUpdateDestroy

urlpatterns = [
    path('list/', OrderListCreate.as_view()),
    path('list/<int:pk>/', OrderRetrieveUpdateDestroy.as_view()),
    path('listunit/', OrderUnitListCreate.as_view()),
    path('listunit/<int:pk>/', OrderUnitRetrieveUpdateDestroy.as_view()),
]
