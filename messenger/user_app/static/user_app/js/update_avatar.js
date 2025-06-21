$(document).ready(function(){
    $("#popupForm").on("submit", function(event){
        event.preventDefault();

        let formData = new FormData(this);

        $.ajax({
            url: this.action,
            type: 'post',
            data: formData,
            processData:false,
            contentType:false,
            success: function(response){
                $('#avatar').attr('src', response.avatar_url)
            }
        })
    })
})