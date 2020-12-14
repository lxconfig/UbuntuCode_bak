
function CompleteEvents() {
    var event_id = $("#event-id").html();
    var req_data = {
        "event_id": event_id
    }
    var req_json = JSON.stringify(req_data);
    $.ajax({
        type: "post",
        url: "/success",
        contentType: "application/json",
        data: req_json,
        dataType: "json",
        success: function (response) {
            if (response.errno == "0") {
                alert(response.errmsg);
                location.herf = "/events";
                $("#success").hide();
            } else {
                alert(response.errmsg);
            }
        }
    });
}


$(function() {
    $.get("/sessions", function(response) {
        if (response.errno == "0") {
            $("#notLogin1").hide();
            $("#notLogin2").hide();
            $("#hasLogin").show();
            $("#islogin").html(response.data.username);
            $("#islogin").show();

        } else {
            $("#notLogin1").show();
            $("#notLogin2").show();
            $("#hasLogin").hide();
        }
    });

    $(".form-signin").submit(function (e) { 
        e.preventDefault();
        var kind_name = $("#kind-name").val();
        if (!kind_name) {
            alert("请填写类别名!");
        }
        var req_data = {
            "kind_name": kind_name
        }
        var req_json = JSON.stringify(req_data);
        $.ajax({
            type: "post",
            url: "/kinds",
            data: req_json,
            contentType: "application/json",
            dataType: "json",
            success: function (response) {
                if (response.errno == "0") {
                    alert(response.errmsg);
                    location.href = "/index.html";
                } else {
                    alert(response.errmsg);
                }
            }
        });
    });

    $(".form-events").submit(function (e) { 
        e.preventDefault();
        var title = $("#events-title").val();
        var kind_id = $("#events-kind").val();
        if (!title) {
            alert("请填写标题");
        } else if (!kind_id) {
            alert("请填写待办类别");
        }
        var req_data = {
            "title": title,
            "kind_id": kind_id
        }
        var req_json = JSON.stringify(req_data);
        $.ajax({
            type: "post",
            url: "/addEvents",
            contentType: "application/json",
            data: req_json,
            dataType: "json",
            success: function (response) {
                if (response.errno == "0") {
                    alert("添加成功");
                    location.href = "/events";
                } else {
                    alert(response.errmsg);
                }
            }
        });
    });
})