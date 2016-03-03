// Miscellaneous JavaScript used on multiple pages

/**
 * Selects the text in a div so the user can easily copy it to the clipboard.
 * @param {Object} div
 */
function selectdiv(div) {
    var doc = document;
    var text = doc.getElementById(div)
    var range;

    if (doc.body.createTextRange) {
        range = doc.body.createTextRange();
        range.moveToElementText(text);
        range.select();
    } else if (window.getSelection) {
        var selection = window.getSelection();
        range = doc.createRange();
        range.selectNodeContents(text);
        selection.removeAllRanges();
        selection.addRange(range);
    }
}

/**
 * Shows the modal with the given citekey, and switches to the given tab.
 * @param {string} citekey
 * @param {string} tab
 */
function showmodaltab(citekey, tab) {
    var m = $("#" + citekey + "cite");
    var t = m.find('a[href="#' + citekey + tab + '"]');
    m.modal('show');
    t.tab('show');
}

// Don't reload the page when clicking on an anchor link
(function($) {
    $('a[href="#"]').click(function(e) {
        e.preventDefault();
    });
})(jQuery);

// Hook up all the tooltips
(function($) {
    $('[data-tooltip]').tooltip();
})(jQuery);

// Use $ for inline math
MathJax.Hub.Config({
    "tex2jax": { inlineMath: [ [ '$', '$' ] ] }
});
