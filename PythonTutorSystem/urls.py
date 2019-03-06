from django.urls import path, include
from PythonTutorSystem import views

urlpatterns = [
    path('Test/', views.test, name='test'),

    # index
    path('', views.index, name='index'),

    # blockly_games
    path('BlocklyGames/', include('PythonTutorSystem.blockly_games_urls')),

    # blockly_lesson
    path('Blockly/Lektion/', include('PythonTutorSystem.blockly_lesson_urls')),

    # blockly_compendium
    path('Blockly/', include('PythonTutorSystem.blockly_compendium_urls')),

    # python_lesson
    path('Python/Lektion/', include('PythonTutorSystem.python_lesson_urls')),

    # python_compendium
    path('Python/', include('PythonTutorSystem.python_compendium_urls')),

    # ide_lesson
    path('IDE/Lektion/', include('PythonTutorSystem.ide_lesson_urls')),

    # footer
    path('About/', views.about, name='about'),
    path('Impressum/', views.impressum, name='impressum'),
    path('Datenschutz/', views.data_protection, name='data_protection'),
    path('Sitemap/', views.sitemap, name='sitemap'),
]
