// Show loading icon until iframe fully loaded
function show_iframe() {
    document.getElementById('blockly_games_iframe').style.visibility = 'visible';
    document.getElementById('loading_icon').style.display = 'none';
}

window.onload(function () {
    if (/Android|webOS|iPhone|iPad|iPod|BlackBerry|BB|PlayBook|IEMobile|Windows Phone|Kindle|Silk|Mobile|Opera Mini/i.test(navigator.userAgent)) {
        document.getElementById('loading_icon').style.display = 'none';
        document.getElementById('blockly_games_iframe').style.display = 'none';
        document.getElementById('mobile_blockly_games').style.display = 'block';
    }
});