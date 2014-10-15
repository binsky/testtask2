$(document).ready(function(){
    $("#sort").click(function(e){
        var data = $("#input").val();
        $("#loading").toggleClass("hidden");
        $.ajax({
            url : "/sort/",
            type : "GET",
            dataType: "json",
            data : {
                input :  data
//                csrfmiddlewaretoken: '{{ csrf_token }}' //for the POST method
            },
            success : function(data) {
                $('#output').val(data.result ? data.result : data.error);
                $("#loading").toggleClass("hidden");
            },
            error : function(xhr,errmsg,err) {
                alert(xhr.status + ": " + xhr.responseText);
                $("#loading").toggleClass("hidden");
            }
        });
        e.preventDefault();
    });
});