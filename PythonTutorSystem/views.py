from django.shortcuts import render


def test(request):
    return render(request, 'test.html')


# index
def index(request):
    return render(request, 'index.html')


# blockly_games
def labyrinth(request):
    return render(request, 'blockly_lesson/blockly_games/labyrinth.html')


def puzzle(request):
    return render(request, 'blockly_lesson/blockly_games/puzzle.html')


def bird(request):
    return render(request, 'blockly_lesson/blockly_games/bird.html')


def turtle(request):
    return render(request, 'blockly_lesson/blockly_games/turtle.html')


def movie(request):
    return render(request, 'blockly_lesson/blockly_games/movie.html')


def pond(request):
    return render(request, 'blockly_lesson/blockly_games/pond.html')


def pond_documentation(request):
    return render(request, 'blockly_lesson/blockly_games/pond_documentation.html')


def pond_documentation_functions(request):
    return render(request, 'blockly_lesson/blockly_games/pond_documentation_functions.html')


# lesson_1
def lesson_1_introduction(request):
    return render(request, 'blockly_lesson/introduction.html')


def lesson_1_blockly_games_explanation(request):
    return render(request, 'blockly_lesson/blockly_games_explanation.html')


def lesson_1_blockly_games_puzzle(request):
    return render(request, 'blockly_lesson/blockly_games_puzzle.html')


def lesson_1_labyrinth_preparation(request):
    return render(request, 'blockly_lesson/labyrinth_preparation.html')


def lesson_1_instructions(request):
    return render(request, 'blockly_lesson/instructions.html')


def lesson_1_conditional_statements(request):
    return render(request, 'blockly_lesson/conditional_statements.html')


def lesson_1_loop(request):
    return render(request, 'blockly_lesson/loop.html')


def lesson_1_blockly_games_labyrinth(request):
    return render(request, 'blockly_lesson/blockly_games_labyrinth.html')


def lesson_1_bird_preparation(request):
    return render(request, 'blockly_lesson/bird_preparation.html')


def lesson_1_variables(request):
    return render(request, 'blockly_lesson/variables.html')


def lesson_1_conditional_statements_addition(request):
    return render(request, 'blockly_lesson/conditional_statements_addition.html')


def lesson_1_logic_and(request):
    return render(request, 'blockly_lesson/logic_and.html')


def lesson_1_blockly_games_bird(request):
    return render(request, 'blockly_lesson/blockly_games_bird.html')


def lesson_1_turtle_preparation(request):
    return render(request, 'blockly_lesson/turtle_preparation.html')


def lesson_1_counting_loop(request):
    return render(request, 'blockly_lesson/counting_loop.html')


def lesson_1_variables_addition(request):
    return render(request, 'blockly_lesson/variables_addition.html')


def lesson_1_functions(request):
    return render(request, 'blockly_lesson/functions.html')


def lesson_1_blockly_games_turtle(request):
    return render(request, 'blockly_lesson/blockly_games_turtle.html')


def lesson_1_movie_preparation(request):
    return render(request, 'blockly_lesson/movie_preparation.html')


def lesson_1_blockly_games_movie(request):
    return render(request, 'blockly_lesson/blockly_games_movie.html')


def lesson_1_pond_preparation(request):
    return render(request, 'blockly_lesson/pond_preparation.html')


def lesson_1_blockly_games_pond(request):
    return render(request, 'blockly_lesson/blockly_games_pond.html')


def lesson_1_pond_solution(request):
    return render(request, 'blockly_lesson/pond_solution.html')


def lesson_1_wrap_up(request):
    return render(request, 'blockly_lesson/wrap_up.html')


# blockly_compendium
def blockly_compendium(request):
    return render(request, 'blockly_compendium/compendium.html')


# python_lesson_exercises
def lesson_2_exercises_variables(request):
    return render(request, 'python_lesson/exercises/exercises_variables.html')


def lesson_2_exercises_strings(request):
    return render(request, 'python_lesson/exercises/exercises_strings.html')


def lesson_2_exercises_print(request):
    return render(request, 'python_lesson/exercises/exercises_print.html')


def lesson_2_exercises_input(request):
    return render(request, 'python_lesson/exercises/exercises_input.html')


def lesson_2_exercises_conditional_statements(request):
    return render(request, 'python_lesson/exercises/exercises_conditional_statements.html')


def lesson_2_exercises_while_loop(request):
    return render(request, 'python_lesson/exercises/exercises_while_loop.html')


def lesson_2_exercises_list(request):
    return render(request, 'python_lesson/exercises/exercises_list.html')


# python_lesson
def lesson_2_introduction(request):
    return render(request, 'python_lesson/introduction.html')


def lesson_2_structuring(request):
    return render(request, 'python_lesson/structuring.html')


def lesson_2_variables(request):
    return render(request, 'python_lesson/variables.html')


def lesson_2_datatypes(request):
    return render(request, 'python_lesson/datatypes.html')


def lesson_2_operators(request):
    return render(request, 'python_lesson/operators.html')


def lesson_2_operators_precedence(request):
    return render(request, 'python_lesson/operators_precedence.html')


def lesson_2_print(request):
    return render(request, 'python_lesson/print.html')


def lesson_2_input(request):
    return render(request, 'python_lesson/input.html')


def lesson_2_conditional_statements(request):
    return render(request, 'python_lesson/conditional statements.html')


def lesson_2_while_loop(request):
    return render(request, 'python_lesson/while_loop.html')


def lesson_2_for_loop(request):
    return render(request, 'python_lesson/for_loop.html')


def lesson_2_strings(request):
    return render(request, 'python_lesson/strings.html')


def lesson_2_list(request):
    return render(request, 'python_lesson/list.html')


def lesson_2_tuple(request):
    return render(request, 'python_lesson/tuple.html')


def lesson_2_set(request):
    return render(request, 'python_lesson/set.html')


def lesson_2_dictionary(request):
    return render(request, 'python_lesson/dictionary.html')


def lesson_2_functions(request):
    return render(request, 'python_lesson/functions.html')


def lesson_2_recursion(request):
    return render(request, 'python_lesson/recursion.html')


def lesson_2_object_oriented_programming(request):
    return render(request, 'python_lesson/object_oriented_programming.html')


def lesson_2_classes(request):
    return render(request, 'python_lesson/classes.html')


def lesson_2_heredity(request):
    return render(request, 'python_lesson/heredity.html')


def python_lesson_wrap_up(request):
    return render(request, 'python_lesson/wrap_up.html')


# python_compendium
def python_compendium(request):
    return render(request, 'python_compendium/compendium.html')


# ide_lesson
def lesson_3_repl_test(request):
    return render(request, 'ide_lesson/repl_test.html')


def ide_lesson_introduction(request):
    return render(request, 'ide_lesson/introduction.html')


def ide_lesson_python_installation(request):
    return render(request, 'ide_lesson/python_installation.html')


def ide_lesson_pycharm_installation(request):
    return render(request, 'ide_lesson/pycharm_installation.html')


def ide_lesson_ipython_installation(request):
    return render(request, 'ide_lesson/ipython_installation.html')


def ide_lesson_modules(request):
    return render(request, 'ide_lesson/modules.html')


def ide_lesson_namespace(request):
    return render(request, 'ide_lesson/namespace.html')


def ide_lesson_exercises(request):
    return render(request, 'ide_lesson/exercises.html')


def ide_lesson_simple_exercise(request):
    return render(request, 'ide_lesson/simple_exercise.html')


# footer
def about(request):
    return render(request, 'footer/about.html')


def impressum(request):
    return render(request, 'footer/impressum.html')


def data_protection(request):
    return render(request, 'footer/data_protection.html')


def sitemap(request):
    return render(request, 'footer/sitemap.html')
