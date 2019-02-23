// Set size of elements to window size
function resizeTopContent(){
    $('.window_size').height( $(window).height() );
    $('.window_size').width( $(window).width() );
}

// Call set size function on window load
$(document).ready(function() {
    resizeTopContent();
});

// Call set size function on window resize
$(window).resize(function() {
    resizeTopContent();
});