from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib import messages

from django.core.mail import send_mail
from django.conf import settings

from django_countries import countries

from video_app.models import Video

from .models import Game, Highlight, RecentGame, UpcomingSchedule

from .forms import CreateGamePostForm, UpdateUserForm

User = get_user_model()


def home_page(request):
    highlight = Highlight.objects.all()
    context = {
        'highlights': highlight
    }
    return render(request, "home/home.html", context)

def search(request):
    query = request.GET['query']
    allVideos = Video.objects.filter(title__icontains=query)
    context = {'allVideos': allVideos}
    return render(request, "home/search.html", context)

def notify(request):
    send_mail('Notification of game', 'The game will start soon, Please watch and enjoy',
                settings.EMAIL_HOST_USER, ['pranilkhadka321@gmail.com'])
    return render(request, "home/notify.html")

def about_us(request):
    return render(request, "home/about-us.html")


def add_game(request):
    context = {}
    user = request.user
    if not user.is_superuser:
        return redirect('home:home-page')

    if request.method == 'POST':
        form = CreateGamePostForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Game added.')
    else:
        form = CreateGamePostForm()
    context['form'] = form
    return render(request, 'home/add-game.html', context)


def all_games(request):
    user = request.user
    if not user.is_authenticated:
        return redirect('user:login')
    games = Game.objects.all()
    context = {
        'games': games
    }
    return render(request, "home/all-games.html", context)


def user_list(request):
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(request, "home/users.html", context)


def admin_area(request):
    return render(request, "home/admin-area.html")


def delete_user(request, user_id):
    user = User.objects.get(id=user_id)
    user.delete()
    return redirect('home:user-list')


def edit_user(request, user_id):
    if request.method == "POST":
        user = User.objects.get(id=user_id)
        form = UpdateUserForm(request.POST or None, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'User updated.')
    else:
        user = User.objects.get(id=user_id)
        form = UpdateUserForm(instance=user)
    context = {
        'form': form,
        'user': user,
        "countries": list(countries)
    }
    return render(request, "home/edit-user.html", context)

def upcoming_view(request):
    photos = UpcomingSchedule.objects.all()
    context = {
        'photos': photos
    }
    return render(request, "home/upcoming.html", context)

def recent_view(request):
    photos = RecentGame.objects.all()
    context = {
        'photos': photos
    }
    return render(request, "home/recent.html", context)