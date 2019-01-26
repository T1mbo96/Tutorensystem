from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required


def test(request):
    return render(request, 'test.html')


# index
def index(request):
    return render(request, 'index.html')


# blockly_games
@login_required
def labyrinth(request):
    return render(request, 'lesson_1/blockly_games/labyrinth.html')


@login_required
def puzzle(request):
    return render(request, 'lesson_1/blockly_games/puzzle.html')


@login_required
def bird(request):
    return render(request, 'lesson_1/blockly_games/bird.html')


@login_required
def turtle(request):
    return render(request, 'lesson_1/blockly_games/turtle.html')


@login_required
def movie(request):
    return render(request, 'lesson_1/blockly_games/movie.html')


@login_required
def pond(request):
    return render(request, 'lesson_1/blockly_games/pond.html')


@login_required
def pond_documentation(request):
    return render(request, 'lesson_1/blockly_games/pond_documentation.html')


@login_required
def pond_documentation_functions(request):
    return render(request, 'lesson_1/blockly_games/pond_documentation_functions.html')


# lesson_1
@login_required
def lesson_1_introduction(request):
    return render(request, 'lesson_1/introduction.html')


@login_required
def lesson_1_blockly_games_explanation(request):
    return render(request, 'lesson_1/blockly_games_explanation.html')


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
def lesson_1_bird_preparation(request):
    return render(request, 'lesson_1/bird_preparation.html')


@login_required
def lesson_1_variables(request):
    return render(request, 'lesson_1/variables.html')


@login_required
def lesson_1_conditional_statements_addition(request):
    return render(request, 'lesson_1/conditional_statements_addition.html')


@login_required
def lesson_1_logic_and(request):
    return render(request, 'lesson_1/logic_and.html')


@login_required
def lesson_1_blockly_games_bird(request):
    return render(request, 'lesson_1/blockly_games_bird.html')


@login_required
def lesson_1_turtle_preparation(request):
    return render(request, 'lesson_1/turtle_preparation.html')


@login_required
def lesson_1_counting_loop(request):
    return render(request, 'lesson_1/counting_loop.html')


@login_required
def lesson_1_variables_addition(request):
    return render(request, 'lesson_1/variables_addition.html')


@login_required
def lesson_1_functions(request):
    return render(request, 'lesson_1/functions.html')


@login_required
def lesson_1_blockly_games_turtle(request):
    return render(request, 'lesson_1/blockly_games_turtle.html')


@login_required
def lesson_1_blockly_games_movie(request):
    return render(request, 'lesson_1/blockly_games_movie.html')


@login_required
def lesson_1_pond_preparation(request):
    return render(request, 'lesson_1/pond_preparation.html')


@login_required
def lesson_1_blockly_games_pond(request):
    return render(request, 'lesson_1/blockly_games_pond.html')


@login_required
def lesson_1_pond_solution(request):
    return render(request, 'lesson_1/pond_solution.html')


@login_required
def lesson_1_wrap_up(request):
    return render(request, 'lesson_1/wrap_up.html')


# lesson_2_exercises
@login_required
def lesson_2_exercises_variables(request):
    return render(request, 'lesson_2/exercises/exercises_variables.html')


@login_required
def lesson_2_exercises_strings(request):
    return render(request, 'lesson_2/exercises/exercises_strings.html')


@login_required
def lesson_2_exercises_print(request):
    return render(request, 'lesson_2/exercises/exercises_print.html')


@login_required
def lesson_2_exercises_input(request):
    return render(request, 'lesson_2/exercises/exercises_input.html')


@login_required
def lesson_2_exercises_conditional_statements(request):
    return render(request, 'lesson_2/exercises/exercises_conditional_statements.html')


@login_required
def lesson_2_exercises_while_loop(request):
    return render(request, 'lesson_2/exercises/exercises_while_loop.html')


@login_required
def lesson_2_exercises_list(request):
    return render(request, 'lesson_2/exercises/exercises_list.html')


# lesson_2
@login_required
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


# lesson_3
@login_required
def lesson_3_repl_test(request):
    return render(request, 'lesson_3/repl_test.html')


# footer
def about(request):
    return render(request, 'footer/about.html')


def impressum(request):
    return render(request, 'footer/impressum.html')


def data_protection(request):
    return render(request, 'footer/data_protection.html')


def sitemap(request):
    return render(request, 'footer/sitemap.html')
