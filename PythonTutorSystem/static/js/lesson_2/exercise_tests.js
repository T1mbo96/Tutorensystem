// Variables
function variables_test_code() {
    runit();
    var _output = document.getElementById('output').innerText;
    if(_output==="50\n") {
        show_success_alert();
    } else {
        show_danger_alert();
    }
}

// Strings
function strings_test_code() {
    runit();
    var _output = document.getElementById('output').innerText;
    if(_output==="Hallo, Welt!\n,\nH\n!\n") {
        show_success_alert();
    } else {
        show_danger_alert();
    }
}

// Print-Function
function print_test_code() {
    runit();
    var _output = document.getElementById('output').innerText;
    if(_output==="Variable 10\nVariable&3.5\nVariable!") {
        show_success_alert();
    } else {
        show_danger_alert();
    }
}

// Input-Function
function input_test_code() {
    runit();
    var _output = document.getElementById('output').innerText;
    if(_output==="532\n") {
        show_success_alert();
    } else {
        show_danger_alert();
    }
}