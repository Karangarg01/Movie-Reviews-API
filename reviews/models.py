from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    release_year = models.IntegerField()

    class Meta:
        unique_together = ('title', 'release_year')  # prevents duplicates

    def __str__(self):
        return self.title


class Review(models.Model):
    movie = models.ForeignKey(Movie, related_name="reviews", on_delete=models.CASCADE)
    reviewer = models.CharField(max_length=100)
    rating = models.IntegerField()  # scale 1–10
    comment = models.TextField()

    def __str__(self):
        return f"{self.reviewer} - {self.movie.title}"
