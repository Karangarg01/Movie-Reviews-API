from django.contrib import admin
from .models import Movie, Review

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'release_year')  # show these fields in the list
    search_fields = ('title', 'genre')  # search box in admin
    list_filter = ('genre', 'release_year')  # filters on the right side


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('movie', 'reviewer', 'rating')
    search_fields = ('movie__title', 'reviewer')
    list_filter = ('rating',)
