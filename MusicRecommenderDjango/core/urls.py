from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('search/', views.search, name='search'),
]
