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
        var reply_boxes = $('.comment .comment-form-wrapper');
        var comment = $(this).closest('.comment');
        var comment_id = comment.attr('data-id');

        reply_boxes.removeClass('show');

        form_html =  '<form action="/comments/' + comment_id + '/reply/" method="POST">';
        form_html += '<input name="csrfmiddlewaretoken" type="hidden" value="'+ getCookie('csrftoken') +'" />';
        form_html += '<input name="comment-id" type="hidden" value="'+ comment_id +'" />';
        form_html += '<textarea name="comment-content" rows="3"></textarea>';
        form_html += '<button type="submit">Submit</button>'
        form_html += '</form>';

        comment.find('.comment-form-wrapper[data-id="'+comment_id+'"]').html(form_html)
    });

})( jQuery );