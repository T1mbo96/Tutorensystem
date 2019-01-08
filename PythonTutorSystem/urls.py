from django.urls import path, include
from PythonTutorSystem import views

urlpatterns = [
    path('Test/', views.test, name='test'),

    # index
    path('Home/', views.index, name='index'),

    # blockly_games
    path('Blockly_Games/', include('PythonTutorSystem.blockly_games_urls')),

    # lesson_1
    path('Lektion_1/', include('PythonTutorSystem.lesson_1_urls')),

    # lesson_2
    path('Lektion_2/', include('PythonTutorSystem.lesson_2_urls')),

    # footer
    path('About/', views.about, name='about'),
    path('Impressum/', views.impressum, name='impressum'),
    path('Datenschutz/', views.data_protection, name='data_protection'),
    path('Sitemap/', views.sitemap, name='sitemap'),
]
