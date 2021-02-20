from django.urls import path

from order.views import OrderListCreate, OrderRetrieveUpdateDestroy, order_form_dependencies

urlpatterns = [
    path('list/', OrderListCreate.as_view()),
    path('list/<int:pk>/', OrderRetrieveUpdateDestroy.as_view()),
    path('order-form-dependencies/', order_form_dependencies),

]
