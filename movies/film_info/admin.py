from django.contrib import admin

# Register your models here.
from .models import Film, Review


class FilmAdmin(admin.ModelAdmin):
    fields = [("film_title", "year", "genre")]




class ReviewAdmin(admin.ModelAdmin):
    fields = ["summary", "review", "review_film"]


admin.site.register(Film)
admin.site.register(Review)
