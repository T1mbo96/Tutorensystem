// Variables
function variables_test_code() {
    let solution_array = ["50"];
    test_code(solution_array);
}

// Strings
function strings_test_code() {
    let solution_array = ["Hallo, Welt!", ",", "a", "!"];
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
    let solution_array = ["Sehr gut! Sie haben ein Puzzle gewonnen!"];
    test_code(solution_array);
}

// While-Loop
function while_loop_test_code() {
    let solution_array = ["10", "8", "6", "4", "2", "0"];
    test_code(solution_array);
}

// List
function list_test_code() {
    let min = 1;
    let max = 1000;
    let even_numbers = [];
    let odd_numbers = [];
    let mixed_numbers = [];

    // Generate a list of 10 random numbers for mixed_numbers
    for (let counter = 0; counter < 10; counter++) {
        let random = Math.floor(Math.random() * (+max - +min)) + +min;

        if (random % 2 === 0) {
            even_numbers.push(random);
        } else {
            odd_numbers.push(random);
        }

        mixed_numbers.push(random);
    }

    // Add the generated numbers to this hidden div, so that the function getEditorCode() (skulpt.js) can use the list
    document.getElementById('mixed_numbers').innerHTML = mixed_numbers.toString();

    let even_numbers_str = "[";
    even_numbers_str += even_numbers.toString().split(',').join(', ');
    even_numbers_str += "]";

    let odd_numbers_str = "[";
    odd_numbers_str += odd_numbers.toString().split(',').join(', ');
    odd_numbers_str += "]";

    let solution_array = [even_numbers_str, odd_numbers_str];
    test_code(solution_array);
}

// Prime
function prime_test_code() {
    let solution_array = ["Die 1. Primzahl ist: 2", "Die 2. Primzahl ist: 3", "Die 3. Primzahl ist: 5", "Die 4. Primzahl ist: 7", "Die 5. Primzahl ist: 11", "Die 6. Primzahl ist: 13", "Die 7. Primzahl ist: 17", "Die 8. Primzahl ist: 19", "Die 9. Primzahl ist: 23", "Die 10. Primzahl ist: 29"];
    test_code(solution_array);
}

// Functions
function functions_test_code() {
    let solution_array = ["[2, 3, 5, 8, 10, 12, 14, 23, 27, 35, 100, 102]", "[6, 7, 9, 13, 17, 43, 58, 76, 89, 120, 125, 224]", "[4, 5, 6, 7, 17, 22, 23, 25, 33, 58, 122, 323]", "[5, 6, 45, 67, 78, 122, 164, 899, 1003, 2456, 14609, 203789]"]
    test_code(solution_array);
}

// Test output of the user implemented code
function test_code(solution_array) {
    runit();
    let output_array = document.getElementById('output').innerText.split("\n");
    let template_array = [];

    // Generate array that has as many indices as available alerts
    for (let counter = 0; counter < solution_array.length; counter++) {
        if (counter < output_array.length) {
            template_array[counter] = output_array[counter];
        } else {
            template_array.push("");
        }
    }

    // Show success or fail alerts
    for (let counter = 0; counter < template_array.length; counter++) {
        if (template_array[counter] === solution_array[counter]) {
            show_numbered_success_alert(counter + 1);
        } else {
            show_numbered_danger_alert(counter + 1);
        }
    }
}

// Show success alert and hide fail alert
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

// Show fail alert and hide success alert
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

// Reset value of editor to default
function reset_skulpt() {
    var text = document.getElementById("custom_code").value;
    editor.setValue(text);
}