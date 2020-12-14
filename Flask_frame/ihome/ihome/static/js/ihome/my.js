function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");  // 通过正则匹配，获取cookie中csrf_token的值 \b代表单词边界
    return r ? r[1] : undefined;  // r[1] if r else None;
}

function logout() {
    $.ajax({
        url: "/api/v1.0/session",
        type: "delete",
        headers: {
            "X-CSRFToken": getCookie("csrf_token")
        },
        dataType: "json",
        success: function (response) {
            if (response.errno == "0") {
                location.href = "/index.html";
            }
        }
    })
}

$(document).ready(function(){
    $.get("/api/v1.0/users/info", function (response) {
        if (response.errno == "0") {
            $("#user-avatar").attr("src", response.data.avatar_url);
            $("#user-name").html(response.data.user_name);
            $("#user-mobile").html(response.data.mobile);
        } else {
            alert(response.errmsg);
        }
    }, "json");
})