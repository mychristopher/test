$(function () {
    $("#my_form").submit(function () {
        var u_name = $("#u_name").val();
        if(u_name.length <= 3) {
            alert("用户名不能小于三位");
            return false
        }
        if ($("#pwd").val() != $("#c_pwd").val() || $("#pwd").val().length <= 3){
            alert('密码两次不一致或过短');
            return false;
        } else {
            //加密 并将加密结果写到input标签里
            var pwd = md5($("#pwd").val());
            $("#pwd").html(pwd);

            var c_pwd = md5($("#c_pwd").val());
            $("#c_pwd").html(c_pwd);
        }
    })
});