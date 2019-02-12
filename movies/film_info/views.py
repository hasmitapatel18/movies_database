from django.shortcuts import render, redirect

from django.http import HttpResponse

from .models import Film

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import login, logout, authenticate

from django.contrib import messages


def homepage(request):
    return render(request=request, template_name="film_info/home.html", context={"all_movies": Film.objects.all()})

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username= form.cleaned_data.get('username')
            messages.success(request, f"New Account Created: {username}")
            login(request, user)
            return redirect("film_info:homepage")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

    form = UserCreationForm
    return render(request=request, template_name="film_info/register.html", context={"form": form})
