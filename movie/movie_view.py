from movie.models import Movie
from order_app.common.api_views import MovieCreateAPIView


class MovieListCreateAPIView (MovieCreateAPIView):
    queryset = Movie.objects.filter(deleted=False)
    list_serilizer = MovieListSerializer
    write_serilizer = MovieWriteSerializer

