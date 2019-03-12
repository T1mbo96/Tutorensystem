let list_outputs;

function list_outf(text) {
    list_outputs += text;
    list_outputs += '\n';
}

// List
function list_test_code() {
    let solution_array = ["2 3 5 6 7 8 9 10 12 13 14 17 23 27 35 43 58 76 89 100 102 120 125 224"];
    let lists = "unordered_list = [10, 8, 12, 2, 5, 3, 27, 102, 23, 14, 35, 100, 13, 120, 17, 6, 7, 9, 224, 125, 76, 89, 58, 43]\n";

    for (let counter = 0; counter < 3; counter++) {
        var prog = editor.getDoc().getValue();
        let temp = prog.substring(prog.indexOf('#'), prog.length - 1);
        prog = lists;
        prog += temp;
        var mypre = document.getElementById("output");
        mypre.innerHTML = '';
        Sk.pre = "output";
        Sk.configure({output: list_outf, read: builtinRead});
        (Sk.TurtleGraphics || (Sk.TurtleGraphics = {})).target = 'mycanvas';
        var myPromise = Sk.misceval.asyncToPromise(function () {
            return Sk.importMainWithBody("<stdin>", false, prog, true);
        });
        myPromise.then(function (mod) {
                console.log('success');
            },
            function (err) {
                console.log(err.toString());
                list_outf(err.toString());
            });
    }
    mypre.innerHTML = mypre.innerHTML + list_outputs;
    hide_alerts();
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