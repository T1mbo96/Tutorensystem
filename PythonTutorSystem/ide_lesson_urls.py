from django.urls import path
from . import views

urlpatterns = [
    path('Test_Repl/', views.lesson_3_repl_test, name='lesson_3_repl_test'),
    path('Einführung/', views.ide_lesson_introduction, name='ide_lesson_introduction'),
    path('Python/Installation/', views.ide_lesson_python_installation, name='ide_lesson_python_installation'),
    path('PyCharm/Installation/', views.ide_lesson_pycharm_installation, name='ide_lesson_pycharm_installation'),
    path('IPython/Installation/', views.ide_lesson_ipython_installation, name='ide_lesson_ipython_installation'),
    path('Module/', views.ide_lesson_modules, name='ide_lesson_modules'),
    path('Namensraum/', views.ide_lesson_namespace, name='ide_lesson_namespace'),
    path('Aufgaben/', views.ide_lesson_exercises, name='ide_lesson_exercises'),
]
