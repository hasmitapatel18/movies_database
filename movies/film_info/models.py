from django.db import models

# Create your models here.
class Film(models.Model):
    film_title=models.CharField(max_length=200)
    year = models.PositiveSmallIntegerField(blank=True, null=True)
    genre=models.CharField(max_length=100)
    review=models.TextField()

    def __str__(self):
        return self.film_title

    class Meta:
        ordering=['film_title']
