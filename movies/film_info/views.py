from django.shortcuts import render

from django.http import HttpResponse

from .models import Film

def homepage(request):
    return render(request=request, template_name="film_info/home.html", context={"all_movies": Film.objects.all()})
