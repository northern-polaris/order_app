from django.urls import path

from order.views import OrderListCreate, OrderRetrieveUpdateDestroy

urlpatterns = [
    path('list/', OrderListCreate.as_view()),
    path('list/<int:pk>/', OrderRetrieveUpdateDestroy.as_view()),

]
