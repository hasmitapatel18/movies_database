from django.contrib import admin
from django.contrib.auth.models import User

# Register your models here.
from .models import Film, Review, Comment


class FilmAdmin(admin.ModelAdmin):
    fields = [("film_title", "year", "genre")]




class ReviewAdmin(admin.ModelAdmin):
    fields = ["summary", "review", "review_film"]


class CommentAdmin(admin.ModelAdmin):
    fields = ["post", "user", "content", "timestamp"]



admin.site.register(Film)
admin.site.register(Review)
admin.site.register(Comment)
