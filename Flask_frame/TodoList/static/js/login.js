
$(function () {
    $(".form-signin").submit(function (e) { 
        e.preventDefault();
        var mobile = $("#mobile").val();
        var password = $("#password").val();
        if (!mobile || !password) {
            alert("请填写手机号和密码");
            location.href = "login.html";
        }
        var req_data = {
            "mobile": mobile,
            "password": password,
        }
        var req_json = JSON.stringify(req_data);
        $.ajax({
            type: "post",
            url: "/users/login",
            data: req_json,
            contentType: "application/json",
            dataType: "json",
            success: function (response) {
                if (response.errno == "0") {
                    location.href = "index.html";
                } else {
                    alert(response.errmsg);
                    location.href = "login.html";
                }
            }
        });
    });
})