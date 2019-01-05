from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# index
def index(request):
    return render(request, 'index.html')


# blockly_games
@login_required
def labyrinth(request):
    return render(request, 'blockly_games/labyrinth.html')


# lesson_1
@login_required
def lesson_1_introduction(request):
    return render(request, 'lesson_1/introduction.html')


@login_required
def lesson_1_blockly_games_puzzle(request):
    return render(request, 'lesson_1/blockly_games_puzzle.html')


@login_required
def lesson_1_labyrinth_preparation(request):
    return render(request, 'lesson_1/labyrinth_preparation.html')


@login_required
def lesson_1_instructions(request):
    return render(request, 'lesson_1/instructions.html')


@login_required
def lesson_1_conditional_statements(request):
    return render(request, 'lesson_1/conditional_statements.html')


@login_required
def lesson_1_loop(request):
    return render(request, 'lesson_1/loop.html')


@login_required
def lesson_1_blockly_games_labyrinth(request):
    return render(request, 'lesson_1/blockly_games_labyrinth.html')


@login_required
# lesson_2
def lesson_2_introduction(request):
    return render(request, 'lesson_2/introduction.html')


@login_required
def lesson_2_structuring(request):
    return render(request, 'lesson_2/structuring.html')


@login_required
def lesson_2_variables(request):
    return render(request, 'lesson_2/variables.html')


@login_required
def lesson_2_datatypes(request):
    return render(request, 'lesson_2/datatypes.html')


@login_required
def lesson_2_operators(request):
    return render(request, 'lesson_2/operators.html')


@login_required
def lesson_2_operators_precedence(request):
    return render(request, 'lesson_2/operators_precedence.html')


@login_required
def lesson_2_print(request):
    return render(request, 'lesson_2/print.html')


@login_required
def lesson_2_input(request):
    return render(request, 'lesson_2/input.html')


@login_required
def lesson_2_conditional_statements(request):
    return render(request, 'lesson_2/conditional statements.html')


@login_required
def lesson_2_while_loop(request):
    return render(request, 'lesson_2/while_loop.html')


@login_required
def lesson_2_for_loop(request):
    return render(request, 'lesson_2/for_loop.html')


@login_required
def lesson_2_strings(request):
    return render(request, 'lesson_2/strings.html')


@login_required
def lesson_2_list(request):
    return render(request, 'lesson_2/list.html')


@login_required
def lesson_2_tuple(request):
    return render(request, 'lesson_2/tuple.html')


@login_required
def lesson_2_set(request):
    return render(request, 'lesson_2/set.html')


@login_required
def lesson_2_dictionary(request):
    return render(request, 'lesson_2/dictionary.html')


@login_required
def lesson_2_functions(request):
    return render(request, 'lesson_2/functions.html')


@login_required
def lesson_2_recursion(request):
    return render(request, 'lesson_2/recursion.html')


@login_required
def lesson_2_namespace(request):
    return render(request, 'lesson_2/namespace.html')


@login_required
def lesson_2_object_oriented_programming(request):
    return render(request, 'lesson_2/object_oriented_programming.html')


@login_required
def lesson_2_classes(request):
    return render(request, 'lesson_2/classes.html')


@login_required 
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
