var request = $.ajax({
   type: "GET",
   url: "/api/news/"
}).done(function(){
    if (request.status == 200){
         var html = '';
        $.each(request.responseJSON, function(key, value){
            html += '<div class="post-review">';
            html += '<a href="post.html">';
            html += '<h2 class="post-title">' + value.title + '</h2>';
            html += '<h3 class="post-subtitle">' + value.text + '</h2>';
            html += '<p class="post-meta">' +'Username: ' + value.author.username +'</p>';
            html += '</a>';
            html += '</div>';
            html += '<br>';
        });
    $('#content-body').html(html);

    } else {
        console.log("error")}
        console.log(request.status);
    }
);
