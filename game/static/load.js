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

    var celery_loading = function(job_id){
        var csrftoken = getCookie('csrftoken');
        $.ajax({
            type: "GET",
            url: "http://127.0.0.1:8000/game/poll_state/",
            data: {job: job_id, csrfmiddlewaretoken: csrftoken},
        })
        .done(function( data ) {
            //console.log(data);
            if(data['state'].current == "SUCCESS"){
                progressBar_celery.setPercent(1000);
                console.log("FINISH");
                $("#results_celery").remove();
                $(".mot").text(data['state'].result);
                $(".definition").text(data['state'].definition);
            }
            else{
                if(data['state'] != "PENDING"){
                    //console.log(data['state']);
                    progressBar_celery.setPercent(data['state'].current);
                }
                setTimeout(function() {
                    celery_loading( data['job'] );
                    }, 100);
            }
        })
        .fail(function() {
            alert( "error" );
        });
    };
    var job_id = $('.job_id').text();
    var progressBar_celery = new ProgressBar("results_celery", {'width':'250px', 'height':'25px'});
    progressBar_celery.setPercent(0);
    celery_loading(job_id);

});