from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


# registration
class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/sign_up.html'


# index
def index(request):
    return render(request, 'index.html')


# blockly_games
def labyrinth(request):
    return render(request, 'blockly_games/labyrinth.html')


# lesson_1
def lesson_1_introduction(request):
    return render(request, 'lesson_1/introduction.html')


def lesson_1_blockly_games_puzzle(request):
    return render(request, 'lesson_1/blockly_games_puzzle.html')


def lesson_1_labyrinth_preparation(request):
    return render(request, 'lesson_1/labyrinth_preparation.html')


def lesson_1_instructions(request):
    return render(request, 'lesson_1/instructions.html')


def lesson_1_conditional_statements(request):
    return render(request, 'lesson_1/conditional_statements.html')


def lesson_1_loop(request):
    return render(request, 'lesson_1/loop.html')


def lesson_1_blockly_games_labyrinth(request):
    return render(request, 'lesson_1/blockly_games_labyrinth.html')


# lesson_2
def lesson_2_introduction(request):
    return render(request, 'lesson_2/introduction.html')


def lesson_2_structuring(request):
    return render(request, 'lesson_2/structuring.html')


def lesson_2_variables(request):
    return render(request, 'lesson_2/variables.html')


def lesson_2_datatypes(request):
    return render(request, 'lesson_2/datatypes.html')


def lesson_2_operators(request):
    return render(request, 'lesson_2/operators.html')


def lesson_2_operators_precedence(request):
    return render(request, 'lesson_2/operators_precedence.html')


def lesson_2_print(request):
    return render(request, 'lesson_2/print.html')


def lesson_2_input(request):
    return render(request, 'lesson_2/input.html')


def lesson_2_conditional_statements(request):
    return render(request, 'lesson_2/conditional statements.html')


def lesson_2_while_loop(request):
    return render(request, 'lesson_2/while_loop.html')


def lesson_2_for_loop(request):
    return render(request, 'lesson_2/for_loop.html')


def lesson_2_strings(request):
    return render(request, 'lesson_2/strings.html')


def lesson_2_list(request):
    return render(request, 'lesson_2/list.html')


def lesson_2_tuple(request):
    return render(request, 'lesson_2/tuple.html')


def lesson_2_set(request):
    return render(request, 'lesson_2/set.html')


def lesson_2_dictionary(request):
    return render(request, 'lesson_2/dictionary.html')


def lesson_2_functions(request):
    return render(request, 'lesson_2/functions.html')


def lesson_2_recursion(request):
    return render(request, 'lesson_2/recursion.html')


def lesson_2_namespace(request):
    return render(request, 'lesson_2/namespace.html')


def lesson_2_object_oriented_programming(request):
    return render(request, 'lesson_2/object_oriented_programming.html')


def lesson_2_classes(request):
    return render(request, 'lesson_2/classes.html')


def lesson_2_heredity(request):
    return render(request, 'lesson_2/heredity.html')


# footer
def about(request):
    return render(request, 'footer/about.html')


def impressum(request):
    return render(request, 'footer/impressum.html')


def data_protection(request):
    return render(request, 'footer/data_protection.html')


def sitemap(request):
    return render(request, 'footer/sitemap.html')
