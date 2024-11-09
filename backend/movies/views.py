from rest_framework.pagination import PageNumberPagination
from .models import Movie
from .serializers import MovieListSerializer
from rest_framework.generics import ListAPIView

class MoviePagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100

class MovieListView(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieListSerializer
    pagination_class = MoviePagination

