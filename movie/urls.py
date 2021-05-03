from django.urls import path

from movie.movie_view import MovieListCreateAPIView, MovieUpdateRetrieveDestroyAPIView

urlpatterns = [
    path('list/', MovieListCreateAPIView.as_view(), name='order-list-create'),
    path('list/<int:pk>/', MovieUpdateRetrieveDestroyAPIView.as_view()),

]
