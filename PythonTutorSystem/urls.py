from django.urls import path, include
from PythonTutorSystem import views

urlpatterns = [
    path('Test/', views.test, name='test'),

    # index
    path('Home/', views.index, name='index'),

    # blockly_games
    path('BlocklyGames/', include('PythonTutorSystem.blockly_games_urls')),

    # lesson_1
    path('Blockly/Lektion/', include('PythonTutorSystem.blockly_lesson_urls')),

    # lesson_2
    path('Python/Lektion/', include('PythonTutorSystem.python_lesson_urls')),

    # lesson_3
    path('Lektion_3/', include('PythonTutorSystem.lesson_3_urls')),

    # footer
    path('About/', views.about, name='about'),
    path('Impressum/', views.impressum, name='impressum'),
    path('Datenschutz/', views.data_protection, name='data_protection'),
    path('Sitemap/', views.sitemap, name='sitemap'),
]
