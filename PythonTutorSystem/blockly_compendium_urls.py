from django.urls import path
from . import views

urlpatterns = [
    path('Kompendium/', views.blockly_compendium, name='blockly_compendium'),
]
