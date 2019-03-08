$(document).ready(function () {

    $('#sidebarCollapse').on('click', function () {
        $('#sidebar').toggleClass('active');
    });

});

$(document).ready(function () {

    $('#sidebarCollapse').on('click', function () {
        $('#content').toggleClass('active');
    });

});

$(document).ready(function () {

    $("#sidebar").mCustomScrollbar({
        theme: "minimal"
    });

    $('#sidebarCollapse').on('click', function () {
        $('#sidebar').toggleClass('active');
    });

});

$(document).ready(function () {
    $("#sidebar").mCustomScrollbar({
        theme: "minimal",
    });

    $('#sidebarCollapse').on('click', function () {
        // open or close navbar
        $('#sidebar').toggleClass('active');
        // close dropdowns
        $('.collapse.in').toggleClass('in');
        // and also adjust aria-expanded attributes we use for the open/closed arrows
        // in our CSS
        $('a[aria-expanded=true]').attr('aria-expanded', 'false');
    });
});

// Open the respective submenu on page load
$(document).ready(function () {
    if (document.getElementById('submenu_identifier')) {
        var submenu_link = document.getElementById('submenu_identifier').innerText;
        document.getElementById(submenu_link).click();
    }
});


window.onload = function () {
    if (/Android|webOS|iPhone|iPad|iPod|BlackBerry|BB|PlayBook|IEMobile|Windows Phone|Kindle|Silk|Mobile|Opera Mini/i.test(navigator.userAgent)) {
        document.getElementById('mobile').style.marginLeft = '0';
    }
};

