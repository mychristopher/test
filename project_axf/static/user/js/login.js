$(function () {
   $("#my_form").submit(function () {
       var u_name = $("#u_name").val();
       if (u_name.length <= 3){
           alert("用户名过短");
           return false;
       }
       if ($("#pwd").val().length <= 3){
           alert("密码过短");
           return false;
       }
   //    校验通过以后 我们就可以给密码做MD5摘要
       var enc_pwd = md5($("#pwd").val());
       $("#pwd").html(enc_pwd);
   });
});