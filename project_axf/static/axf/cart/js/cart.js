$(function () {
    $(".add_btn").click(function () {
        var $c_btn = $(this);
        var c_id = $c_btn.parents("li").attr("c_id");
        $.ajax({
            url:'/axf/cartitem_change',
            data:{
                o_type: 'add',
                c_id: c_id
            },
            method:'post',
            success: function (res) {
                if (res.code == 1){
                //    更新总价
                    $("#sum_money").html(res.data.sum_money);
                //    更新span数量
                    $c_btn.prev().html(res.data.current_item_num);
                } else {
                    alert(res.msg);
                }
            }
        })
    });

    $(".sub_btn").click(function () {
        var $c_btn = $(this);
        var c_id = $c_btn.parents("li").attr("c_id");
        $.ajax({
            url:'/axf/cartitem_change',
            data:{
                o_type: 'sub',
                c_id: c_id
            },
            method:'post',
            success: function (res) {
                if (res.code == 1){
                //    更新总价
                    $("#sum_money").html(res.data.sum_money);
                //    更新span数量
                    $c_btn.next().html(res.data.current_item_num);
                } else {
                    alert(res.msg);
                }
            }
        })
    });

//    商品选中
    $(".confirm").click(function () {
        var $c_btn = $(this);
        var c_id = $c_btn.parents("li").attr("c_id");
        $.ajax({
            url:'/axf/cart_item_select',
            data:{
                c_id:c_id
            },
            method:"post",
            success: function (res) {
                if (res.code == 1){
                //    改变总价
                    $("#sum_money").html(res.data.money);
                //    改当前商品的状态
                    if (res.data.is_select){
                        $c_btn.find("span").find("span").html("√");
                    } else {
                        $c_btn.find("span").find("span").html("");
                    }
                //    改变全选按钮
                    if (res.data.is_all_select) {
                        $(".all_select>span>span").html("√");
                    } else {
                        $(".all_select>span>span").html("");
                    }
                } else {
                    alert(res.msg)
                }
            }
        })
    });

    $(".all_select").click(function () {
        $.ajax({
            url:'/axf/select_all',
            method:"post",
            success:function (res) {
                if(res.code == 1){
                    $("#sum_money").html(res.data.money);
                    if (res.data.is_all_select){
                        $(".confirm").each(function () {
                            $(this).find("span").find("span").html("√");
                        });
                        $(".all_select>span>span").html("√");
                    } else {
                        $(".all_select>span>span").html("");
                        $(".confirm").each(function () {
                            $(this).find("span").find("span").html("");
                        })
                    }
                //
                }
            }
        })
    });
})