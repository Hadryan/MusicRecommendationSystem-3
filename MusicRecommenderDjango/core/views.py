from django.shortcuts import render
from .models import RecommendedSongs, PopularSongs, ListeningHistory
from .mldata import content


def home(request):
    popular_songs = PopularSongs.objects.all()
    return render(request, "core/index.html", {'popular_songs': popular_songs})


def search(request):
    return render(request, "core/search.html",)


def profile(request):
    recommended_songs = RecommendedSongs.objects.all()
    listening_history = ListeningHistory.objects.all()
    return render(request, "core/profile.html", {'recommended_songs': recommended_songs, 'listening_history': listening_history})
