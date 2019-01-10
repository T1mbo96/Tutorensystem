// Variables
function variables_test_code() {
    let solution_array = ["50"];
    test_code(solution_array);
}

// Strings
function strings_test_code() {
    let solution_array = ["Hallo, Welt!", ",", "H", "!"];
    test_code(solution_array);
}

// Print-Function
function print_test_code() {
    let solution_array = ["Variable 10", "Variable&3.5", "Variable!"];
    test_code(solution_array);
}

// Input-Function
function input_test_code() {
    let solution_array = ["532"];
    test_code(solution_array);
}

// Conditional Statements
function conditional_statements_test_code() {
    let solution_array = ["Sehr gut! Sie haben einen wafer-thin mint gewonnen!"]
    test_code(solution_array);
}

// Template Test-Function
function test_code(solution_array) {
    runit();
    let output_array = document.getElementById('output').innerText.split("\n");
    let template_array = [];

    for (let counter = 0; counter < solution_array.length; counter++) {
        if (counter < output_array.length) {
            template_array[counter] = output_array[counter];
        } else {
            template_array.push("");
        }
    }

    for (let counter = 0; counter < template_array.length; counter++) {
        if (template_array[counter] === solution_array[counter]) {
            show_numbered_success_alert(counter + 1);
        } else {
            show_numbered_danger_alert(counter + 1);
        }
    }
}

function show_numbered_success_alert(number) {
    let numbered_alert_success = 'correct_' + number;
    let numbered_alert_danger = 'wrong_' + number;

    if (document.getElementById(numbered_alert_success).style.display === 'none') {
        if (document.getElementById(numbered_alert_danger).style.display === 'block') {
            document.getElementById(numbered_alert_danger).style.display = 'none';
        }
        document.getElementById(numbered_alert_success).style.display = 'block';
    }
}

function show_numbered_danger_alert(number) {
    let numbered_alert_success = 'correct_' + number;
    let numbered_alert_danger = 'wrong_' + number;

    if (document.getElementById(numbered_alert_danger).style.display === 'none') {
        if (document.getElementById(numbered_alert_success).style.display === 'block') {
            document.getElementById(numbered_alert_success).style.display = 'none';
        }
        document.getElementById(numbered_alert_danger).style.display = 'block';
    }
}