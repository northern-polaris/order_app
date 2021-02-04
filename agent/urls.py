from django.urls import path

from agent.views import CustomerListCreate

urlpatterns = [
    path('list/', CustomerListCreate.as_view()),
]
