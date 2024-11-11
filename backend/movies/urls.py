from django.urls import path
from .views import MovieListView, MovieDetailView, MovieCreateView
urlpatterns = [
    path("", MovieListView.as_view(), name="movie-list"),
    path("<int:pk>/", MovieDetailView.as_view(), name="movie-details"),
    path("create/", MovieCreateView.as_view(), name="movie-create"),
]
