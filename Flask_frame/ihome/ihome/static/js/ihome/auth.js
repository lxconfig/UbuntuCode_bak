function showSuccessMsg() {
    $('.popup_con').fadeIn('fast', function() {
        setTimeout(function(){
            $('.popup_con').fadeOut('fast',function(){}); 
        },1000) 
    });
}


function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}


$(function () {
    // 通过ajax的get方法请求后端
    $.get("/api/v1.0/users/auth", function (response) {
        if (response.errno == "0") {
            $("#real-name").val(response.data.real_name);
            $("#id-card").val(response.data.id_card);
            $("#real-name").attr("disabled", "disabled");
            $("#id-card").attr("disabled", "disabled");
            $("[type='submit']").hide();
        } else {
            // $(".error-msg").hide();
            return;
        }
    });

    $("#form-auth").submit(function (e) {
        e.preventDefault();
        var real_name = $("#real-name").val();
        var id_card = $("#id-card").val();

        if (!real_name || !id_card) {
            $(".error-msg").show();
            return;
        }
        var request_data = {
            real_name: real_name,
            id_card: id_card
        }
        var json_data = JSON.stringify(request_data);
        $.ajax({
            url: "/api/v1.0/users/auth",
            type: "post",
            data: json_data,
            contentType: "application/json",
            dataType: "json",
            headers: {
                "X-CSRFToken": getCookie("csrf_token")
            },
            success: function (response) {
                if (response.errno == "0") {
                    alert(response.errmsg);
                } else {
                    alert(response.errmsg);
                }
            }
        })
    })
})
