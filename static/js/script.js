$(function() {
    $('#btnGetPosts').click(function() {
        $.ajax({
            url: 'getposts',
            data: {uid:$('#uid').val(),querypos:$('#querypos').val()},
            type: 'POST',
            dataType: 'JSON',
            success: function(response) {
                console.log(response);
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});