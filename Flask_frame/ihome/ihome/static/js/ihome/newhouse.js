function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

$(document).ready(function(){
    // 页面一加载，就去发送请求，拿到城区信息
    $.get("/api/v1.0/areas", function (response) {
        if (response.errno == "0") {
            var areas = response.data;
            // for (var i=0;i < areas.length;i++) {
            //     $("#area-id").append('<option value="' + areas[i].area_id + '">' + areas[i].area_name + '</option>');
            // }
            
            // 使用前端js模板来渲染页面, 参数表示渲染标签的id以及数据
            // 其返回结果是html文本
            var html = template("areas-template", {areas: areas})
            // 填充到对应页面的位置
            $("#area-id").html(html);
        } else {
            alert(response.errmsg);
        }
    }, "json");

    $("#form-house-info").submit(function (e) {
        e.preventDefault();

        // 处理表单数据，通过serializeArray()一次性拿出所有表单中的元素
        // 返回的是JSON对象，而不是JSON字符串。[{name:"xxx", value:"yyy"}, {name:"zzz", value:"ccc"}]
        // 所以需要进行转换，这里用map()来遍历然后转换
        var data = {};
        $("#form-house-info").serializeArray().map(function (x) {
            // x就是JSON对象中的每个元素
            data[x.name] = x.value;
        });

        // 由于设施信息是复选框，用上面得方法只能拿到最后勾选得那个，所以要重新获取
        // 用each()方法来遍历，由于前面jquery选择出来的是整个复选框元素，所以不能直接获取到值
        var facility = []
        $(":checked[name=facility]").each(function (index, x) {
            // x就是复选框元素
            facility[index] = $(x).val();
        })
        data.facility = facility;

        // 像后端发送请求
        $.ajax({
            url: "/api/v1.0/houses/info",
            type: "post",
            contentType: "application/json",
            data: JSON.stringify(data),
            dataType: "json",
            headers: {
                "X-CSRFToken": getCookie("csrf_token")
            },
            success: function(response) {
                if (response.errno == "4101") {
                    location.href = "/login.html";
                } else if (response.errno = "0") {
                    // 隐藏基本信息表单
                    $("#form-house-info").hide();
                    // 显示上传图片表单
                    $("#form-house-image").show();
                    $("#house-id").val(response.data.house_id);
                } else {
                    alert(response.errmsg);
                }
            }
        })
    });

    $("#form-house-image").submit(function (e) {
        e.preventDefault();

        $(this).ajaxSubmit({
            url: "/api/v1.0/houses/images",
            type: "post",
            dataType: "json",
            headers: {
                "X-CSRFToken": getCookie("csrf_token")
            },
            success: function (response) {
                if (response.errno == "4101") {
                    location.href = "/login.html";
                } else if (response.errno = "0") {
                    $(".house-image-cons").append('<img src="' + response.data.image_url + '">');
                } else {
                    alert(response.errmsg);
                }
            }
        })
    })
})