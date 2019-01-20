from django.urls import path
from . import views

urlpatterns = [
    path('Puzzle/', views.puzzle, name='puzzle'),
    path('Labyrinth/', views.labyrinth, name='labyrinth'),
    path('Bird/', views.bird, name='bird'),
    path('Turtle/', views.turtle, name='turtle'),
    path('Movie/', views.movie, name='movie'),
    path('Pond/', views.pond, name='pond'),
    path('Pond/Documentation/', views.pond_documentation, name='pond_documentation'),
    path('Pond/Documentation/Functions/', views.pond_documentation_functions, name='pond_documentation_functions'),
]
