function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");  // 通过正则匹配，获取cookie中csrf_token的值 \b代表单词边界
    return r ? r[1] : undefined;  // r[1] if r else None;
}

// 保存图片验证码编号
var imageCodeId = "";

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

function generateImageCode() {
    // 形成图片验证码的后端地址， 设置到页面中，让浏览请求验证码图片
    imageCodeId = generateUUID();  // uuid 全局唯一标识符
    var url = "/api/v1.0/image_codes/" + imageCodeId;
    $(".image-code img").attr("src", url);
}

function sendSMSCode() {
    $(".phonecode-a").removeAttr("onclick");  // 防止用户连点操作
    var mobile = $("#mobile").val();
    if (!mobile) {
        $("#mobile-err span").html("请填写正确的手机号！");
        $("#mobile-err").show();
        $(".phonecode-a").attr("onclick", "sendSMSCode();");
        return;
    } 
    var imageCode = $("#imagecode").val();
    if (!imageCode) {
        $("#image-code-err span").html("请填写验证码！");
        $("#image-code-err").show();
        $(".phonecode-a").attr("onclick", "sendSMSCode();");
        return;
    }
    // 向后端发送ajax请求
    // 构造get请求的参数
    var req_data = {
        image_codes_id: imageCodeId,  // 图片验证码的编号
        image_code: imageCode   // 图片验证码的值
    }
    // 发送请求
    $.get("/api/v1.0/sms_codes/"+mobile, req_data, function (response) {
        // 对返回的结果做判断，要覆盖后端所有的情况，这里只选发送成功和失败的情况
        if (response.errno == "0") {
            // 发送成功，应该把 获取验证码 改为倒计时60s
            var num = 60
            var timer = setInterval(function () {  // 间隔1000毫秒，执行一次function
                if (num > 1){
                    // 修改 获取验证码 文本，进行倒计时
                    $(".phonecode-a").html(num + "秒");
                    num -= 1;
                } else {
                    // 倒计时结束，改回 获取验证码 文本,并重新添加点击事件
                    $(".phonecode-a").html("获取验证码");
                    $(".phonecode-a").attr("onclick", "sendSMSCode();");
                    clearInterval(timer);   // 清除定时器
                }
            }, 1000, 60)
        } else {
            // 后端返回的其他情况
            alert(response.errmsg);
            $(".phonecode-a").attr("onclick", "sendSMSCode();");
        }
    });
}

$(document).ready(function() {
    generateImageCode();
    $("#mobile").focus(function(){
        $("#mobile-err").hide();
    });
    $("#imagecode").focus(function(){
        $("#image-code-err").hide();
    });
    $("#phonecode").focus(function(){
        $("#phone-code-err").hide();
    });
    $("#password").focus(function(){
        $("#password-err").hide();
        $("#password2-err").hide();
    });
    $("#password2").focus(function(){
        $("#password2-err").hide();
    });
    $(".form-register").submit(function(e){
        e.preventDefault();  // 表示阻止事件的默认行为，这里就是阻止submit提交
        // 获取用户填写的数据
        var mobile = $("#mobile").val();
        var image_code = $("#imagecode").val();
        var sms_code = $("#phonecode").val();
        var password = $("#password").val();
        var password2 = $("#password2").val();

        // 验证数据完整性
        if (!mobile) {
            $("#mobile-err").html("请填写手机号!");
            $("#mobile-err").show();
            return;
        }
        if (!image_code) {
            $("#image-code-err").html("请填写图片验证码!");
            $("#image-code-err").show();
            return;
        }
        if (!sms_code) {
            $("#phone-code-err").html("请填写短信验证码!");
            $("#phone-code-err").show();
            return;
        }
        if (!password) {
            $("#password-err").html("请填写密码!");
            $("#password-err").show();
            return;
        }
        if (password !== password2) {
            $("#password2-err").html("两次密码不一致!");
            $("#password2-err").show();
            return;  
        }
        // 发送ajax请求
        // 定义请求数据
        var request_data = {
            mobile: mobile,
            sms_code: sms_code,
            password: password,
            password2: password2
        };
        // 转换为json格式
        var json_data = JSON.stringify(request_data);
        // 发送请求
        $.ajax({
            url: "/api/v1.0/users",
            type: "post",
            data: json_data,
            contentType: "application/json",
            dataType: "json",
            headers: {
                "X-CSRFToken": getCookie("csrf_token")  // 由于CSRFProtect只能获取form表单数据的值，或请求头中的 X-CSRFToken 字段
            },
            success: function (response) {
                if (response.errno == "0") {
                    // 注册成功
                    location.href = "/index.html";
                } else {
                    alert(response.errmsg);
                }
            }
        })
    });
})