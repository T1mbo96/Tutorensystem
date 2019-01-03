from django.urls import path
from . import views

urlpatterns = [
    path('Einführung/', views.lesson_2_introduction, name='lesson_2_introduction'),
    path('Strukturierung/', views.lesson_2_structuring, name='lesson_2_structuring'),
    path('Variablen/', views.lesson_2_variables, name='lesson_2_variables'),
    path('Datentypten/', views.lesson_2_datatypes, name='lesson_2_datatypes'),
    path('Operatoren/', views.lesson_2_operators, name='lesson_2_operators'),
    path('Operatoren_Priorität/', views.lesson_2_operators_precedence, name='lesson_2_operators_precedence'),
    path('Print/', views.lesson_2_print, name='lesson_2_print'),
    path('Input/', views.lesson_2_input, name='lesson_2_input'),
    path('Bedingte_Anweisungen/', views.lesson_2_conditional_statements, name='lesson_2_conditional_statements'),
    path('while_Schleife/', views.lesson_2_while_loop, name='lesson_2_while_loop'),
    path('for_Schleife/', views.lesson_2_for_loop, name='lesson_2_for_loop'),
    path('Strings/', views.lesson_2_strings, name='lesson_2_strings'),
    path('Liste/', views.lesson_2_list, name='lesson_2_list'),
    path('Tupel/', views.lesson_2_tuple, name='lesson_2_tuple'),
    path('Set/', views.lesson_2_set, name='lesson_2_set'),
    path('Dictionary/', views.lesson_2_dictionary, name='lesson_2_dictionary'),
    path('Funktionen/', views.lesson_2_functions, name='lesson_2_functions'),
    path('Rekursion/', views.lesson_2_recursion, name='lesson_2_recursion'),
    path('Namensraum/', views.lesson_2_namespace, name='lesson_2_namespace'),
    path('Objektorientiertes_Programmieren/', views.lesson_2_object_oriented_programming, name='lesson_2_object_oriented_programming'),
    path('Klassen/', views.lesson_2_classes, name='lesson_2_classes'),
    path('Vererbung/', views.lesson_2_heredity, name='lesson_2_heredity'),
]
