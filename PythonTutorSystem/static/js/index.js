$(".jumbotron").css({height: $(window).height() + "px"});

$(window).on("resize", function () {
    $(".jumbotron").css({height: $(window).height() + "px"});
});

function smooth_scroll() {
    document.querySelector('#scroll_anchor').scrollIntoView({
        behavior: 'smooth'
    });
}