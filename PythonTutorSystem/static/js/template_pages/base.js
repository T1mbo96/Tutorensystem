// Open dropdown links in navbar when hovered
function toggleDropdown(e) {
    const _d = $(e.target).closest('.dropdown'),
        _m = $('.dropdown-menu', _d);
    setTimeout(function () {
        const shouldOpen = e.type !== 'click' && _d.is(':hover');
        _m.toggleClass('show', shouldOpen);
        _d.toggleClass('show', shouldOpen);
        $('[data-toggle="dropdown"]', _d).attr('aria-expanded', shouldOpen);
        // Time till dropdown closes
    }, e.type === 'mouseleave' ? 50 : 0);
}

$('body')
    .on('mouseenter mouseleave', '.dropdown', toggleDropdown)
    .on('click', '.dropdown-menu a', toggleDropdown);

// Delay showing the animated content until everything loaded
$(document).ready(function () {
    if (document.getElementById('load_animation_div')) {
        document.getElementById('load_animation_div').style.visibility = 'visible';
    }
});

