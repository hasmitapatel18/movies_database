from django.shortcuts import render, redirect, get_object_or_404

from django.http import HttpResponse, HttpResponseRedirect

from .models import Film, Review, Comment

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.contrib.auth import login, logout, authenticate

from django.contrib import messages

from .forms import NewUserForm, CommentForm, FilmForm, ReviewForm

from django.template import loader

from django.core.exceptions import ObjectDoesNotExist

from django.forms import modelformset_factory

from django.views.decorators.http import require_POST



def homepage(request):
    return render(request=request, template_name="film_info/home.html", context={"all_movies": Film.objects.all()})




def reviewpage(request, review_id):

    rpage = Review.objects.get(id=review_id)
    film_id = rpage.review_film.id
    cpage = Comment.objects.filter(post=film_id)

    if request.method == "POST":
        form = CommentForm(request.POST or None)

        if form.is_valid():
            cpage = Comment.objects.filter(post=film_id)
            content=request.POST.get('content')
            cc=Comment.objects.create( post_id=film_id, user=request.user, content=content)

            cc.save()

            form=CommentForm()
    else:
        form=CommentForm()

    context={'rpage':rpage, 'cpage':cpage, 'form':form}
    return render(request=request, template_name="film_info/reviewpage.html", context=context)



def filmformpage(request):

    if request.method == "POST":
        fform = FilmForm(request.POST, request.FILES)

        if fform.is_valid():
            film_title=request.POST.get('film_title')
            year=request.POST.get('year')
            genre=request.POST.get('genre')
            image = fform.cleaned_data['image']


            ff=Film.objects.create(film_title=film_title, year=year, genre=genre, image=image)
            ff.save()
    else:
        fform=FilmForm()

    if request.method == "POST":
        rform = ReviewForm(request.POST, request.FILES)

        if rform.is_valid():
            summary=request.POST.get('summary')
            review=request.POST.get('review')

            rf=Review.objects.create( summary=summary)
            rf.review=review
            rf.review_film_id=ff.id
            rf.save()
    else:
        rform=ReviewForm()

    context={'fform':fform, 'rform':rform}
    return render(request=request, template_name="film_info/filmformpage.html", context=context)




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
