from django.db import models

# Create your models here.
class Film(models.Model):
    film_title=models.CharField(max_length=200)
    year = models.PositiveSmallIntegerField(blank=True, null=True)
    genre=models.CharField(max_length=100)




    def __str__(self):
        return self.film_title

    class Meta:
        ordering=['film_title']

    def get_queryset(self):
        return Film.objects.all()


class Review(models.Model):
    summary=models.TextField(null=True)
    review=models.TextField()
    review_film=models.OneToOneField(Film, default=1, primary_key=True, on_delete = models.SET_DEFAULT)



    def __str__(self):
        return self.summary

    def get_queryset(self):
        return Review.objects.all()
