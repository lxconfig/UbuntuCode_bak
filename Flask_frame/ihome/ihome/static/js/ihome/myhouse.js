$(document).ready(function(){
    $.get("/api/v1.0/users/auth",function (response) {
        if (response.errno == "4101") {
            // 用户未登录
            location.href = "/login.html";
        } else if (response.errno == "4002") {
            // 用户没有实名认证
            $(".auth-warn").show();
            return;
        }
        // 已经实名的用户，就获取他们的房源信息
        $.get("/api/v1.0/users/houses", function (response) {
            if (response.errno == "0") {
                // 用前端js框架渲染页面
                var html = template("houses-list-template", {houses:response.data.houses});
                $("#houses-list").html(html);
            } else {
                var html = template("houses-list-template", {houses:[]});
                $("#houses-list").html(html);
            }
        })
    });

    
})