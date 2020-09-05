$(function () {
    //全部类型标签的点击事件
    var is_down = true;
    var is_sort_down = true;
    $("#all_type").click(function () {
        $("#type_container").toggle();
    //    判断is_down的状态
        is_down = change_type_status(is_down);
    });
    $("#type_container").click(function () {
        $(this).toggle();
        is_down = change_type_status(is_down);
    });

    $("#all_sort").click(function () {
        $("#sort_container").toggle();
        is_sort_down = change_sort_status(is_sort_down);
    })
    $("#sort_container").click(function () {
        $(this).toggle();
        is_sort_down = change_sort_status(is_sort_down);
    });
//    给商品的加号添加点击事件
    $(".addShopping").click(function () {
        //prop 只能获得系统的属性 无法获得自定属性的值
        var g_id = $(this).attr('g_id');
        //记录当前点击的按钮元素
        var $current_btn = $(this);
        //发送请求给后端
        $.ajax({
            url:"/axf/cart_api",
            data:{
                g_id: g_id,
                opreate_type:"add",
                //通过DJANGO的csrf校验
                csrfmiddlewaretoken: $.cookie("csrftoken"),
            },
            method:"post",
            success:function (res) {
                if (res.code == 1) {
                    var num = res.data;
                    //拿到加号前边的那个span标签 更新商品的数量
                    $current_btn.prev().html(num);
                }
                else if (res.code == 2){
                    //如果没登陆 需要跳转到登录页面
                    window.open(url=res.data, target="_self");
                }

            }
        })
    });
//    给商品的减号添加点击事件
    $(".subShopping").click(function () {
        //prop 只能获得系统的属性 无法获得自定属性的值
        var g_id = $(this).attr('g_id');
        var $current_btn = $(this);
        //商品数量是0 点操作不允许
        if ($(this).next().val() == '0') {
            return;
        }
        $.ajax({
            url:"/axf/cart_api",
            data:{
                g_id: g_id,
                opreate_type:"sub",
                csrfmiddlewaretoken: $.cookie("csrftoken"),
            },
            method:"post",
            success:function (res) {
                if (res.code == 1) {
                    var num = res.data;
                    //更新商品的数量
                    $current_btn.next().html(num);
                }
                else if (res.code == 2){
                    //如果没登陆 需要跳转到登录页面
                    window.open(url=res.data, target="_self");
                }

            }
        })
    });
})

function change_type_status(is_down) {
    if (is_down == true){
            $("#all_type>span").removeClass("glyphicon-chevron-down").addClass("glyphicon-chevron-up");
            is_down = false;
        } else {
            $("#all_type>span").removeClass("glyphicon-chevron-up").addClass("glyphicon-chevron-down");
            is_down = true;
        }
    return is_down;
}

function change_sort_status(is_down) {
    if (is_down == true){
            $("#all_sort>span").removeClass("glyphicon-chevron-down").addClass("glyphicon-chevron-up");
            is_down = false;
        } else {
            $("#all_sort>span").removeClass("glyphicon-chevron-up").addClass("glyphicon-chevron-down");
            is_down = true;
        }
    return is_down;
}