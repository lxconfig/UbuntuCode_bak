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
    $("#form-avatar").submit(function (e) {
        e.preventDefault();
        // 发送的数据由ajaxSubmit来处理，回调函数由我们来写
        // 普通的ajax，再发请求时，data字段不好处理
        $(this).ajaxSubmit({
            url: "/api/v1.0/users/avatar",
            type: "post",
            dataType: "json",
            headers: {
                "X_CSRFToken": getCookie("csrf_token")
            },
            success: function (response) {
                if (response.errno == "0") {
                    // 上传成功
                    var avatar_url = response.data.avatar_url;
                    $("#user-avatar").attr("src", avatar_url);
                } else {
                    alert(response.errmsg);
                }
            }
        })
    });

    $("#form-name").submit(function (e) {
        e.preventDefault();
        var name = $("#user-name").val();

        if (!name) {
            $(".error-msg").html("请填写用户名");
            $(".error-msg").show();
            return;
        }

        var request_data = {
            name: name
        }
        var json_data = JSON.stringify(request_data);
        $.ajax({
            url: "/api/v1.0/users/name",
            type: "post",
            data: json_data,
            contentType: "application/json",
            dataType: "json",
            headers: {
                "X-CSRFToken": getCookie("csrf_token")
            },
            success: function (response) {
                if (response.errno == "0") {
                    alert("修改成功");
                    $("#user-name").attr("value", response.data.user_name);
                    // location.href = "/my.html";
                } else {
                    alert(response.errmsg);
                }
            }
        })
    })

})
