from django.shortcuts import render, redirect

from django.http import HttpResponse

from .models import Film, Review

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.contrib.auth import login, logout, authenticate

from django.contrib import messages

from .forms import NewUserForm

# def single_slug(request, single_slug):
#     reviewss = [r.review_slug for r in Film.objects.all()]
#     if single_slug in reviewss:
#       return HttpResponse(f"{single_slug} is a category")
#     return HttpResponse(f"'{single_slug}' does not correspond to anything we know of!")

def homepage(request):
    return render(request=request, template_name="film_info/home.html", context={"all_movies": Film.objects.all()})

def reviewpage(request):
    return render(request=request, template_name="film_info/reviewpage.html", context={"all_reviews": Review.objects.all()})


def filminstance(request):
    Review.objects.filter(associatedrev=film_film_title.id)
    return render(request, 'reviewpage.html', associatedrev=associatedrev)




def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username= form.cleaned_data.get('username')
            messages.success(request, f"New Account Created: {username}")
            login(request, user)
            messages.info(request, f"You are now logged in as {username}")
            return redirect("film_info:homepage")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

    form = NewUserForm
    return render(request=request, template_name="film_info/register.html", context={"form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "Logged out")
    return redirect("film_info:homepage")


def login_request(request):
    if request.method == "POST":
        form= AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect("film_info:homepage")
            else:
                messages.error(request, "Invalid Username or Password")
        else:
            messages.error(request, "Invalid Username or Password")
    form = AuthenticationForm()
    return render(request, "film_info/login.html", {"form":form})
