"""Defines URL patterns for web."""
from django.urls import path
from . import views

urlpatterns = [
    #Home page
    path('', views.index, name='index'),
    # Albums page
    path('albums/', views.albums, name='albums'),
    # Detail page for a single album
    path('albumdetail/<int:album_id>/', views.albumdetail, name='albumdetail'),
]

