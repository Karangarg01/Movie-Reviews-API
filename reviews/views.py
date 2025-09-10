from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Avg
from .models import Movie, Review
from .serializers import MovieSerializer, ReviewSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    # Custom endpoint: /api/movies/<id>/rating/
    @action(detail=True, methods=["get"])
    def rating(self, request, pk=None):
        movie = self.get_object()
        avg = movie.reviews.aggregate(Avg("rating"))["rating__avg"]
        return Response({"movie": movie.title, "average_rating": round(avg, 2) if avg else None})


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
