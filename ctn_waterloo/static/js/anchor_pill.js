// This script allows URL hashes (anchors) to be associated with
// the corresponding navigation pills.

// Taken from http://stackoverflow.com/
// questions/12131273/twitter-bootstrap-tabs-url-doesnt-change

// if hash in URL on page load, navigate to hash
var hash = window.location.hash;
if (hash)
    $('ul.nav a[href="' + hash + '"]').tab('show');

// change the hash when we click a pill
$('a[data-toggle="pill"]').click(function (e) {
    $(this).tab('show');
    var scrollmem = $('body').scrollTop();
    window.location.hash = this.hash;
    $('html,body').scrollTop(scrollmem);
});

// Taken from http://stackoverflow.com/
// questions/2161906/handle-url-anchor-change-event-in-js
if ("onhashchange" in window) { // event supported?
    window.onhashchange = function () {
        hashChanged(window.location.hash);
    }
}
else { // event not supported:
    var storedHash = window.location.hash;
    window.setInterval(function () {
        if (window.location.hash != storedHash) {
            storedHash = window.location.hash;
            hashChanged(storedHash);
        }
    }, 100);
}

// when hash changes, click the associated pill
function hashChanged(storedHash) {
    $('a[href="' + storedHash + '"]').click();
}
