// Save value of editor in localStorage when page gets closed or refreshed
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

// Populate editor with value of localStorage if available when page loads
window.onload = function () {
    var key;
    if (document.getElementById("local_storage_key")) {
        key = document.getElementById("local_storage_key").innerText;
    }
    if (localStorage[key]) {
        editor.setValue(localStorage[key]);
    }
};

