var editor;
var lists_editor;
Sk.python3 = true;

// Print output of user implemented code
function outf(text) {
    var mypre = document.getElementById("output");
    mypre.innerHTML = mypre.innerHTML + text;
}

function builtinRead(x) {
    if (Sk.builtinFiles === undefined || Sk.builtinFiles["files"][x] === undefined)
        throw "File not found: '" + x + "'";
    return Sk.builtinFiles["files"][x];
}

function getEditorCode() {
    let prog;

    // Functions exercise -> add the lists to the code
    if (document.getElementById('functions_lists_code')) {
        prog = document.getElementById('functions_lists_code').innerHTML;
        prog += editor.getDoc().getValue();
    }

    // List exercise -> add generated numbers of hidden div to mixed_numbers
    if (document.getElementById('mixed_numbers')) {
        let temp = editor.getDoc().getValue();
        let insert_index = temp.indexOf('[');
        prog = temp.slice(0, insert_index + 1) + document.getElementById('mixed_numbers').innerHTML + temp.slice(insert_index + 1);
    }

    return prog;
}

// Run user implemented code
function runit() {
    let prog;

    if (document.getElementById('functions_lists_code') || document.getElementById('mixed_numbers')) {
        // Add additional necessary code for lists and functions exercise
        prog = getEditorCode();
    } else {
        // Get code of user
        prog = editor.getDoc().getValue();
    }

    var mypre = document.getElementById("output");
    mypre.innerHTML = '';
    Sk.pre = "output";
    Sk.configure({output: outf, read: builtinRead});
    (Sk.TurtleGraphics || (Sk.TurtleGraphics = {})).target = 'mycanvas';
    var myPromise = Sk.misceval.asyncToPromise(function () {
        return Sk.importMainWithBody("<stdin>", false, prog, true);
    });
    myPromise.then(function (mod) {
            console.log('success');
        },
        function (err) {
            console.log(err.toString());
            outf(err.toString());
        });
    hide_alerts();
}

// Hide all alerts that indicate a wrong or right answer
function hide_alerts() {
    let alert_array = document.getElementsByClassName('_alert');

    for (let counter = 0; counter < alert_array.length; counter++) {
        alert_array[counter].style.display = 'none';
    }
}

// Wrap Skulpt editor with CodeMirror
$(document).ready(function () {
    if (document.getElementById('custom_code')) {
        var code = $("#custom_code")[0];
        editor = CodeMirror.fromTextArea(code, {
            lineNumbers: true,
            mode: "python",
        });
    }

    if (document.getElementById('functions_lists_code')) {
        var lists_code = $("#functions_lists_code")[0];
        lists_editor = CodeMirror.fromTextArea(lists_code, {
            lineNumbers: true,
            mode: "python",
        });

        lists_editor.setOption('readOnly', 'true');
    }
});