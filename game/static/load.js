function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


$( document ).ready(function() {

    $( ".ajax_celery" ).on( "click", function() {
        var progressBar_celery = new ProgressBar("results_celery", {'width':'250px', 'height':'25px'});
        progressBar_celery.setPercent(0);
    });
});