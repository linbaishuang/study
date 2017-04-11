/**
 * Created by admin on 2017/3/28.
 */

$(function () {
    $("input[type='file']").val("");
    $.post("colum_info", function (data) {
        var jsonData = $.parseJSON(data);
        var dataStr = "<option value='0'>请选择</option>";
        for(i in jsonData){
            dataStr += "<option value='" + jsonData[i].columnId + "'>" +
                    jsonData[i].name + "</option>"
        }
        $("select[name='select']").empty().append(dataStr);
    })
});

//提交被点击的时候出发事件
$("body").on("click", "input[name='submit']", function () {
    $("#pictureForm").attr("action", "save_picture");

    $("#pictureForm").ajaxSubmit({
        //是否重置表单
        resetForm: false,
        //传递值的类型
        dataType: 'json',
        //成功之后做的事情
        success:function (data) {
            if(data == 0){
                alert("失败");
            }else if(data == 1){
                alert("成功");
                window.location.href = "img_form";
            }
        }
    });
});

//判断图片类型
function judgePicture(){
	var file = $('#pictureFile').val();
	if(/.(gif|jpg|jpeg|png|gif|jpg|png)$/.test(file)){
	    return 1;
	}else{
	    return 0;
	 }
}

//获取本地的url
function getFileUrl(fileId) {
    var url;
    var file = document.getElementById(fileId);
    var agent = navigator.userAgent;
    if (agent.indexOf("MSIE")>=1) {
    url = file.value;
    } else if(agent.indexOf("Firefox")>0) {
    url = window.URL.createObjectURL(file.files.item(0));
    } else if(agent.indexOf("Chrome")>0) {
    url = window.URL.createObjectURL(file.files.item(0));
    }
    return url;
}

//修改img的src属性
$("body").on("change", "input[type='file']", function () {
    if(judgePicture() == 0){
        alert("图片格式为.gif,jpeg,jpg,png中的一种");
        $("input[type='file']").val("");
    }else{
        var url = getFileUrl("pictureFile");
        $("#image").attr("src", url);
    }
});
