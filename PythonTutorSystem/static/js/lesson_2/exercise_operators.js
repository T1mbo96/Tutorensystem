function test_first() {
    test_solution('12', 'first')
}

function test_second() {
    test_solution('True', 'second')
}

function test_third() {
    test_solution('7', 'third')
}

function test_fourth() {
    test_solution('True', 'fourth')
}

function test_fifth() {
    test_solution('22', 'fifth')
}

function test_sixth() {
    test_solution('True', 'sixth')
}

function test_solution(solution, identifier) {
    if (document.getElementsByName(identifier + 'Radios')) {
        let values = document.getElementsByName(identifier + 'Radios');

        for (let counter = 0; counter < values.length; counter++) {
            if (values[counter].checked) {
                if(solution === values[counter].value) {
                    document.getElementById(identifier + 'Test').style.backgroundColor = 'rgba(17, 166, 17, 0.2)';
                    console.log(values[counter].value);
                    return;
                }
            }
        }

        document.getElementById(identifier + 'Test').style.backgroundColor = 'rgba(166, 17, 17, 0.2)'
    }
}