from rest_framework import serializers
from .models import Movie, Review
from django.db.models import Avg

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = '__all__'

    def get_average_rating(self, obj):
        avg = obj.reviews.aggregate(Avg("rating"))["rating__avg"]
        return round(avg, 2) if avg else None

    def validate(self, data):
        title = data.get("title")
        release_year = data.get("release_year")
        if Movie.objects.filter(title__iexact=title, release_year=release_year).exists():
            raise serializers.ValidationError(
                f"The movie '{title}' ({release_year}) already exists in the list."
            )
        return data

