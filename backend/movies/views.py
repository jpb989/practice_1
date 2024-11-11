from rest_framework.pagination import PageNumberPagination
from .models import Movie
from .serializers import MovieListSerializer, MovieSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView
from accounts.authentication import BlacklistTokenAuthentication
from accounts.permission import IsStaffUser
from drf_spectacular.utils import extend_schema

class MoviePagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100


class MovieListView(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieListSerializer
    pagination_class = MoviePagination


class MovieDetailView(RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieCreateView(CreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    authentication_classes = [BlacklistTokenAuthentication]
    permission_classes = [IsStaffUser]


class MovieDeleteView(DestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    authentication_classes = [BlacklistTokenAuthentication]
    permission_classes = [IsStaffUser]

class MovieUpdateView(UpdateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    authentication_classes = [BlacklistTokenAuthentication]
    permission_classes = [IsStaffUser]
