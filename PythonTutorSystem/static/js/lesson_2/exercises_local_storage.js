window.onbeforeunload = function () {
    var key;
    if (document.getElementById("custom_code")) {
        var text = editor.getDoc().getValue();
        if (document.getElementById("local_storage_key")) {
            key = document.getElementById("local_storage_key").innerText;
        }
        localStorage.setItem(key, text);
    }
};

window.onload = function () {
    var key;
    if (document.getElementById("local_storage_key")) {
        key = document.getElementById("local_storage_key").innerText;
    }
    if (localStorage[key]) {
        editor.setValue(localStorage[key]);
    }
};

