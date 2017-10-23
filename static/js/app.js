function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


(function( $ ) {
  
    $('.reply-comment').on('click', function(e) {
        e.preventDefault();

        var comment = $(this).closest('.comment');
        var comment_id = comment.attr('data-id');

        form_template = $('#reply_form_template').html();

        comment.find('.comment-form-wrapper[data-id="'+comment_id+'"]').html(
            _.template(form_template)({
                comment_id: comment_id,
            })
        )
    });

    $('.like').on('click', function(e){
        e.preventDefault();

        var entity = $(this).closest('.entity');
        var model_label = entity.attr('data-model');
        var obj_id = entity.attr('data-id');

        // $.ajax({
        //     url: '/'
        // });
    });

})( jQuery );