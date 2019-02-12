from django.contrib import admin

# Register your models here.
from .models import Film

class FilmAdmin(admin.ModelAdmin):
    fields = ["film_title", "year", "genre", "review"]

admin.site.register(Film)
