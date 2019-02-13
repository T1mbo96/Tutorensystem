$(".jumbotron").css({height: $(window).height() + "px"});

$(window).on("resize", function () {
    $(".jumbotron").css({height: $(window).height() + "px"});
});

// Smooth scroll of let's go button to bottom of page
function smooth_scroll() {
    document.querySelector('#scroll_anchor').scrollIntoView({
        behavior: 'smooth'
    });
}


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