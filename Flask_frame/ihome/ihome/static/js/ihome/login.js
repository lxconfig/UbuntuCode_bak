function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

$(document).ready(function() {
    $("#mobile").focus(function(){
        $("#mobile-err").hide();
    });
    $("#password").focus(function(){
        $("#password-err").hide();
    });
    $(".form-login").submit(function (e) {
        e.preventDefault();
        var mobile = $("#mobile").val();
        var password = $("#password").val();

        if (!mobile) {
            $("#mobile-err").html("请填写手机号");
            $("#mobile-err").show();
            return;
        }
        if (!password) {
            $("#password-err").html("请填写密码");
            $("#password-err").show();
            return;
        }

        // 向后端发送登录请求
        var request_data = {
            mobile: mobile,
            password: password
        }
        var json_data = JSON.stringify(request_data);
        $.ajax({
            url: "/api/v1.0/login",
            type: "post",
            data: json_data,
            contentType: "application/json",
            dataType: "json",
            headers: {
                "X-CSRFToken": getCookie("csrf_token")
            },
            success: function (response) {
                if (response.errno == "0"){
                    location.href = "/index.html"
                } else {
                    alert(response.errmsg);
                }
            }
        })
    })
})