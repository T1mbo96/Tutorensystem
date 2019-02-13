function resizeTopContent(){
    $('.test_wh').height( $(window).height() );
    $('.test_wh').width( $(window).width() );
}

$(document).ready(function() {
    resizeTopContent();
});

$(window).resize(function() {
    resizeTopContent();
});