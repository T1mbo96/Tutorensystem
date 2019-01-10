var editor;
Sk.python3 = true;

function outf(text) {
    var mypre = document.getElementById("output");
    mypre.innerHTML = mypre.innerHTML + text;
}

function builtinRead(x) {
    if (Sk.builtinFiles === undefined || Sk.builtinFiles["files"][x] === undefined)
        throw "File not found: '" + x + "'";
    return Sk.builtinFiles["files"][x];
}

function runit() {
    var prog = editor.getDoc().getValue();
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

function hide_alerts() {
    let alert_array = document.getElementsByClassName('_alert');

    for (let counter = 0; counter < alert_array.length; counter++) {
        alert_array[counter].style.display = 'none';
    }
}

$(document).ready(function () {
    //code here...
    var code = $("#custom_code")[0];
    editor = CodeMirror.fromTextArea(code, {
        lineNumbers: true,
        mode: "python",
    });
});