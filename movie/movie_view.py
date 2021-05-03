from movie.models import Movie
from movie.movie_serializer import MovieListSerializer, MovieWriteSerializer
from order_app.common.api_views import ParentRetrieveUpdateDestroyAPIView, ParentListCreateAPIView


class MovieListCreateAPIView(ParentListCreateAPIView):
    queryset = Movie.objects.filter(deleted=False)
    list_serializer_class = MovieListSerializer
    write_serializer_class = MovieWriteSerializer


class MovieUpdateRetrieveDestroyAPIView(ParentRetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.filter(deleted=False)
    write_serializer_class = MovieWriteSerializer


