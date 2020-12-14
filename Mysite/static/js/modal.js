function showModal() {
    // 移除遮罩层和数据层的hide，使其显示出来
    $("#shadow").removeClass("hide");
    $("#modal").removeClass("hide");
    
}

function cancelModal() {
    // 添加遮罩层和数据层的hide，使其隐藏起来
    $("#shadow").addClass("hide");
    $("#modal").addClass("hide");
    $("#Editmodal").addClass("hide");
}

function EditModal(ths) {
    $("#shadow").removeClass("hide");
    $("#Editmodal").removeClass("hide");
    // 1. 先找到当前元素(对话框编辑)
    // 2. 然后找到其父元素td
    // 3. 再找到td之前所有同级的td，就是caption和id所在的标签
    // 4. 最后赋值给输入框即可
    var row = $(ths).parent().prevAll();
    var content = $(row[1]).text();
    $("#EditTitle").val(content);

    var content_id = $(row[2]).text();
    $("#EditId").val(content_id);
    console.log(content_id, content);

 }

function AjaxSend() {
    var name = $("#title").val();
    $.ajax({
        url: "/show/modal_add_class",
        type: "post",
        data: {"name": name},
        success: function (response) { 
            if (response == "OK") {
                alert("添加成功");
                location.href = "/show/classes";
            } else {
                $("#errorMsg").html(response);
            }
        }
    })
}

function AjaxEdit() {
    var nid = $("#EditId").val();
    var title = $("#EditTitle").val();
    $.ajax({
        type: "post",
        url: "/show/modal_edit_class",
        data: {'nid': nid, 'title': title},
        success: function (response) {
            response = JSON.parse(response);
            if (response.status) {
                location.reload();
            } else {
                alert(response.errormsg);
            }
        }
    });
}