from django.urls import path
from . import views


urlpatterns = [
    path('Labyrinth/', views.labyrinth, name='labyrinth'),
]