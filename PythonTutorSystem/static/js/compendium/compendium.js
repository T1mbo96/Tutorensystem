// Highlights the chosen section from sidenav
function highlight_active_section(identifier, lesson_id) {
    reset_highlighted_sections(lesson_id);
    document.getElementById(identifier).style.backgroundColor = 'rgba(17, 166, 17, 0.2)';
}

// Resets the highlighting of the sections
function reset_highlighted_sections(lesson_id) {
    let sections;

    if (lesson_id === 'python') {
        sections = ['variables_id', 'datatypes_id', 'strings_id', 'operators_id', 'print_id', 'input_id', 'conditional_statements_id', 'while_loop_id', 'for_loop_id', 'lists_id', 'tuple_id', 'set_id', 'dictionary_id', 'functions_id', 'recursion_id', 'classes_id'];
    } else if (lesson_id === 'blockly') {
        sections = ['instructions_id', 'conditional_statements_id', 'loop_id', 'variables_id', 'logic_and_id', 'counting_loop_id', 'functions_id'];
    } else {
        console.log('No compendium identifier defined');
    }
    sections.forEach(function (entry) {
        document.getElementById(entry).style.backgroundColor = '#ffffff';
    })
}

// Delay and scroll 1px down so that every animation is loaded correctly
window.onload = function () {
    setTimeout(function () {
        window.scrollBy(0, 1)
    }, 500);
};
