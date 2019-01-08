// Variables
function variables_test_code() {
    test_code("50\n");
}

// Strings
function strings_test_code() {
    test_code("Hallo, Welt!\n,\nH\n!\n");
}

// Print-Function
function print_test_code() {
    test_code("Variable 10\nVariable&3.5\nVariable!");
}

// Input-Function
function input_test_code() {
    test_code("532\n");
}

// Conditional Statements
function conditional_statements_test_code() {
    test_code("Sehr gut! Sie haben einen wafer-thin mint gewonnen!\n");
}

// Template Test-Function
function test_code(solution) {
    runit();
    var _output = document.getElementById('output').innerText;
    if(_output===solution) {
        show_success_alert();
    } else {
        show_danger_alert();
    }
}