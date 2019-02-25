from django.urls import path
from . import views

urlpatterns = [
    path('Kompendium/', views.python_compendium, name='python_compendium'),
]

