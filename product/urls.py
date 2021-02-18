from django.urls import path

from product.views import ProductListCreate, ProductRetrieveUpdateDestroy, CategoryList

urlpatterns = [
    path('list/', ProductListCreate.as_view()),
    path('list/<int:pk>/', ProductRetrieveUpdateDestroy.as_view()),
    path('list/category/', CategoryList.as_view()),
]
