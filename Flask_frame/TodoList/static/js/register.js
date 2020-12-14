function generateUUID() {
    var d = new Date().getTime();
    if(window.performance && typeof window.performance.now === "function"){
        d += performance.now(); //use high-precision timer if available
    }
    var uuid = 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
        var r = (d + Math.random()*16)%16 | 0;
        d = Math.floor(d/16);
        return (c=='x' ? r : (r&0x3|0x8)).toString(16);
    });
    return uuid;
}

var imgID = null;

function getimgCode() {
    imgID = generateUUID();
    var url = "/users/imgCode?imgID=" + imgID;
    $(".image-code img").attr("src", url);
}


function sendSMSCode() {
    var mobile = $("#mobile").val();
    var imgCode = $("#img-code").val();
    if (!mobile) {
        alert("请填写手机号");
    }
    if (!imgCode) {
        alert("请填写图片验证码");
    }
    var req_data = {
        "mobile": mobile,
        "imgCode": imgCode
    }
    var req_json = JSON.stringify(req_data)
    var url = "/users/smsCode?imgID=" + imgID;
    $.ajax({
        type: "post",
        url: url,
        data: req_json,
        contentType: "application/json",
        dataType: "json",
        success: function (response) {
            if (response.errno == "0") {
                alert("发送成功");
            } else {
                alert(response.errmsg);
                location.reload();
            }
        }
    });
}


$(function(){
    getimgCode();
    $("#verifyImg").click(function () {
        getimgCode();
    });

    $(".form-signin").submit(function (e) { 
        e.preventDefault();
        var username = $("#username").val();
        var mobile = $("#mobile").val();
        var email = $("#inputEmail").val();
        var sms_code = $("#sms_code").val();
        var pwd = $("#password").val();
        var pwd2 = $("#password2").val();
        if (!username) {
            alert("请填写用户名");
        }
        else if (!mobile) {
            alert("请填写手机号");
        }
        else if (!email) {
            alert("请填写邮箱");
        }
        else if (!sms_code) {
            alert("请填写短信验证码");
        }
        else if(!pwd) {
            alert("请填写密码");
        }
        else if (!pwd2) {
            alert("请填写确认密码");
        }
        var req_data = {
            "username": username,
            "mobile": mobile,
            "email": email,
            "sms_code": sms_code,
            "pwd": pwd,
            "pwd2": pwd2
        }
        var req_json = JSON.stringify(req_data);
        $.ajax({
            type: "post",
            url: "/users/register",
            data: req_json,
            contentType: "application/json",
            dataType: "json",
            success: function (response) {
                if (response.errno == "0") {
                    alert("注册成功");
                    location.href = "index.html";
                }
                else {
                    alert(response.errmsg);
                }
            }
        });
    });
})
