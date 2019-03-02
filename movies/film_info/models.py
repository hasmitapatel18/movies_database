

from django.db import models
from django.contrib.auth.models import User

from django.conf import settings
from django.urls import reverse

class Film(models.Model):
    film_title=models.CharField(max_length=200)
    year = models.PositiveSmallIntegerField(blank=True, null=True)
    genre=models.CharField(max_length=100)
    image = models.ImageField(upload_to = 'media/', blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.film_title

    class Meta:
        ordering=['film_title']

    def get_queryset(self):
        return Film.objects.all()


class Review(models.Model):
    summary=models.TextField(null=True)
    review=models.TextField()
    review_film=models.ForeignKey(Film, default=1, on_delete = models.SET_DEFAULT)

    def __str__(self):
        return self.summary


    def get_queryset(self):
        return Review.objects.all()


class Comment(models.Model):
    post = models.ForeignKey(Film, default=1, on_delete = models.SET_DEFAULT)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete = models.SET_DEFAULT)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.post

    def __str__(self):
        return self.content

    def get_queryset(self):
        return Comment.objects.all()

    # def __str__(self):
    #     return 'Comment by {} on {}'.format(self.user, self.post)

    class Meta:
        ordering = ('timestamp',)
