from django.urls import path
from .views import MovieListView, MovieDetailView, MovieCreateView, MovieDeleteView, MovieUpdateView
urlpatterns = [
    path("", MovieListView.as_view(), name="movie-list"),
    path("<int:pk>/", MovieDetailView.as_view(), name="movie-details"),
    path("create/", MovieCreateView.as_view(), name="movie-create"),
    path("delete/<int:pk>", MovieDeleteView.as_view(), name="movie-delete"),
    path("update/<int:pk>", MovieUpdateView.as_view(), name="movie-update"),
]
