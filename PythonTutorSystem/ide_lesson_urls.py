from django.urls import path
from . import views

urlpatterns = [
    path('Test_Repl/', views.lesson_3_repl_test, name='lesson_3_repl_test'),
]