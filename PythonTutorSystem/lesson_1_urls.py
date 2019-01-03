from django.urls import path
from . import views

urlpatterns = [
    path('Einführung/', views.lesson_1_introduction, name='lesson_1_introduction'),
    path('Blockly_Games_Puzzle', views.lesson_1_blockly_games_puzzle, name='lesson_1_blockly_games_puzzle'),
    path('Labyrinth_Vorbereitungen/', views.lesson_1_labyrinth_preparation, name='lesson_1_labyrinth_preparation'),
    path('Anweisungen/', views.lesson_1_instructions, name='lesson_1_instructions'),
    path('Bedingte_Anweisungen/', views.lesson_1_conditional_statements, name='lesson_1_conditional_statements'),
    path('Schleifen/', views.lesson_1_loop, name='lesson_1_loop'),
    path('Blockly_Games_Labyrinth/', views.lesson_1_blockly_games_labyrinth, name='lesson_1_blockly_games_labyrinth'),
]
