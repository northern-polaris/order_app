from django.urls import path

from product.views import ProductListCreate, ProductRetrieveUpdateDestroy

urlpatterns = [
    path('list/', ProductListCreate.as_view()),
    path('list/<int:pk>/', ProductRetrieveUpdateDestroy.as_view()),
]
