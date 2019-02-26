// Highlights the chosen section from sidenav
function highlight_active_section(identifier) {
    reset_highlighted_sections();
    document.getElementById(identifier).style.backgroundColor = 'rgba(17, 166, 17, 0.2)';
}

// Resets the highlighting of the sections
function reset_highlighted_sections() {
    let sections = ['variables_id', 'datatypes_id', 'strings_id', 'operators_id', 'print_id', 'input_id', 'conditional_statements_id', 'while_loop_id', 'for_loop_id', 'lists_id', 'tuple_id', 'set_id', 'dictionary_id', 'functions_id', 'recursion_id', 'namespace_id', 'oop_id', 'classes_id', 'heredity_id'];
    sections.forEach(function (entry) {
        document.getElementById(entry).style.backgroundColor = '#ffffff';
    })
}