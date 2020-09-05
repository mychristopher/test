from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import *
from .my_util import get_select_money


DEFALUT_SORT = 0 # 综合排序
PRICE_SORT = 1 # 按价格排序
SALENUM_SORT = 2 #按销量排序

SUCCESS = 1
NOT_LOGIN = 2
NO_GOODS = 3

# Create your views here.

def home(req):
    # 获取顶部轮播数据
    wheels = MyWheel.objects.raw("SELECT * FROM axf_wheel")
    # 拿导航的数据
    navs = MyNav.objects.all()

    # 把必购的数据查询出来返回给前端
    mustbuys = MustBuy.objects.all()

    # 商店数据
    shops = MyShop.objects.all()
    # 拿到主要信息
    main_shows = MainShow.objects.all()
    data = {
        'title': '首页',
        'swipers': wheels,
        'navs': navs,
        'mustbuys': mustbuys,
        'shop_img': shops[0],
        'shop_1_3': shops[1:3],
        'shop_3_7': shops[3:7],
        'shop_7_11': shops[7:],
        'main_shows': main_shows
    }
    return render(req, 'home/home.html', data)

# 闪购的API
def market(req, c_id, sub_c_id, order_by_type):
    # 拿到全部的分类数据
    all_types = GoodsType.objects.all()

    # 在商品表 去获取对应分类下的数据
    goods_data = MyGoods.objects.filter(categoryid=int(c_id))

    # 如果二级子分类的id 不是0 那么 我们需要在一级分类查询出的数据 再进行过滤
    if (int(sub_c_id) != 0):
        goods_data = goods_data.filter(childcid=int(sub_c_id))

    # 一定是先根据一 二级分类排序以后 去做排序
    order_by_type = int(order_by_type)
    if order_by_type == PRICE_SORT:
        goods_data = goods_data.order_by("price")

    elif order_by_type == SALENUM_SORT:
        # 根据销量排序
        goods_data = goods_data.order_by("productnum")
    else:
        pass


    # 拿当前用户点击的那个分类数据
    current_type = all_types.get(typeid=c_id)
    # 拿二级分类的字符串
    # 低端
    # sub_type_str = current_type.childtypenames
    # sub_type_array = sub_type_str.split("#")
    # res_types = []
    # for i in sub_type_array:
    #     tmp = i.split(":")
    #     res_types.append(tmp)
    # 稍微好一点的写法
    res_types = [i.split(":") for i in current_type.childtypenames.split("#")]
    print(res_types)
    data = {
        'title': "闪购",
        'all_types': all_types,
        'goods_data': goods_data,
        'current_c_id': c_id, #返回用户点击那个分类id
        'sub_types': res_types,
        'current_sub_c_id': sub_c_id,# 返回用户当前点击的二级分类数据\
        'sort_type': order_by_type
    }
    return render(req, 'market/market.html', data)

@login_required(login_url='/axf/login')
def cart(req):
    # 拿用户
    user = req.user
    # 获取该用户的购物车数据
    cart_items = Cart.objects.filter(user_id=user.id)
    # 判断是否全选
    is_selected_all = True #默认是全选
    if cart_items.filter(is_select=False).exists():
        is_selected_all = False

    # 算钱

    data = {
        'user': user,
        'cart_items': cart_items,
        'title': "购物车",
        'is_all_select': is_selected_all,
        'sum_money': get_select_money(user)
    }
    return render(req, 'cart/cart.html', data)

# @login_required(login_url="/axf/login")
def mine(req):
    user = req.user
    is_login = False
    u_name = ""
    u_icon = ""
    if isinstance(user, MyUser):
        is_login = True
        u_name = user.username
        u_icon = user.icon.url
    data = {
        'title': '我的',
        'login_status': is_login,
        'u_name': u_name,
        'icon': "/static/uploads/" + u_icon
    }
    return render(req, 'mine/mine.html', data)


def register(req):
    if req.method == "GET":
        return render(req, 'user/register.html')
    else:
        param = req.POST
        icon_file = req.FILES['u_icon']
        u_name = param.get('u_name')
        pwd = param.get('pwd')
        confirm_pwd = param.get('confirm_pwd')
        email = param.get('email')
        if u_name and pwd and pwd==confirm_pwd and len(u_name)>3:
            # 判断用户是否被注册 .exists() 是看你查询的数据集是否为空 如果数据集为空返回的是false 有数据就返回true
            if MyUser.objects.filter(username=u_name).exists():
                return HttpResponse("该用户已经被注册")
            else:
                MyUser.objects.create_user(
                    username=u_name,
                    password=pwd,
                    email=email,
                    icon=icon_file
                )
                return redirect("axf:mine")
        return redirect("axf:mine")


def login_api(req):
    if req.method == "GET":
        return render(req, 'user/login.html')
    else:
        params = req.POST
        u_name = params.get("u_name")
        pwd = params.get("pwd")
        # 数据格式校验
        if u_name and pwd and len(u_name) > 3:
            # 做用户校验
            user = authenticate(username=u_name, password=pwd)
            if user:
                # 校验通过以后 让用户登录
                login(req, user)
                # 跳转到 我的 页面
                return redirect(reverse("axf:mine"))
            else:
                return redirect(reverse("axf:login"))
        else:
            return HttpResponse("密码过短")

def logout_api(req):
    logout(req)
    return redirect(reverse("axf:mine"))


def cart_api(req):
    user = req.user
    data = {}
    if not isinstance(user, MyUser):

        data["code"] = NOT_LOGIN
        data["msg"] = "未登录"
        data["data"] = "/axf/login"
        return JsonResponse(data)
    # 拿参数
    param = req.POST
    g_id = param.get("g_id")
    opreate_type = param.get("opreate_type")

    # 拿对应的商品
    goods = MyGoods.objects.get(pk=int(g_id))
    cart_item = Cart.objects.filter(
        user=user,
        goods=goods
    )
    # 判断库存
    if goods.storenums <= 0:
        data['code'] = NO_GOODS
        data['msg'] = "库存不足"
        data['data'] = ""
        return JsonResponse(data)
    goods_num = 0
    if opreate_type == 'add':
        if cart_item.exists():
            # 拿到对应购物车商品的信息
            my_cart_item = cart_item.first()
            my_cart_item.num += 1
            my_cart_item.save()
            goods_num = my_cart_item.num
        else:
            Cart.objects.create(
                user=user,
                goods=goods
            )
            goods_num = 1
        data['code'] = SUCCESS
        data['msg'] = "ok"
        data['data'] = goods_num
        return JsonResponse(data)
    else:
        # 减操作
        item = cart_item.first()
        # 购物车商品数量减一
        item.num -= 1
        item.save()
        goods_num = item.num
        if item.num <= 0:
            # 如果商品数量减到0 那我们直接删除数据
            item.delete()
        data['code'] = SUCCESS
        data['msg'] = 'ok'
        data['data'] = goods_num
        return JsonResponse(data)


def cart_item_change(req):
#     拿用户
    user = req.user
    data = {}
# 拿操作类型
    o_type = req.POST.get("o_type")
    c_id = int(req.POST.get('c_id'))
    # 拿到购物车商品数据
    cart_item = Cart.objects.get(pk=c_id)
    if o_type == "add":
#         判断库存
        if cart_item.goods.storenums < 1:

            data['code'] = NO_GOODS
            data['msg'] = "当前商品库存不足"
            data['data'] = ''
            return JsonResponse(data)
        cart_item.num += 1
        cart_item.save()
#         算钱
        sum_money = get_select_money(user)

        data['code'] = SUCCESS
        data['msg'] = 'ok'
        data['data'] = {
            'sum_money': sum_money,
            'current_item_num': cart_item.num
        }
        return JsonResponse(data)
    else:
#         减操作
        cart_item.num -= 1
        cart_item.save()
        if cart_item.num == 0:
            # 如果数量减到0 那我们需要删除商品数据
            cart_item.delete()
#         算钱
        money = get_select_money(user)
        data['code'] = SUCCESS
        data['msg'] = 'ok'
        data['data'] = {
                'sum_money': money,
                'current_item_num': cart_item.num
        }
        return JsonResponse(data)


# 3购物车商品选中
def select_cart_item(req):
    user = req.user
    c_id = int(req.POST.get("c_id"))
#     拿购物车数据
    cart_item = Cart.objects.get(pk=c_id)
    cart_item.is_select = not cart_item.is_select
    cart_item.save()
#     算钱
    money = get_select_money(user)
#     判断全选按钮状态
    is_selected_all = True #默认是全选
    if Cart.objects.filter(user=user, is_select=False).exists():
        is_selected_all = False
    data = {}
    data['code'] = SUCCESS
    data['msg'] = 'ok'
    data['data'] = {
        'is_select': cart_item.is_select,
        'money': money,
        'is_all_select': is_selected_all
    }
    return JsonResponse(data)

def select_all(req):
    user = req.user
    # 判断商品是不是全选

    un_select_items = Cart.objects.filter(
        user=user,
        is_select=False
    )
    is_select_all = True
    if un_select_items.count() == 0:
        # 说明当前是全选， 将所有的用户购物车商品变成全不选
        Cart.objects.filter(user=user).update(is_select=False)
        is_select_all = False
    else:
        un_select_items.update(is_select=True)
        is_select_all = True
    money = get_select_money(user)
    data = {}
    data['code'] = SUCCESS
    data['msg'] = 'ok'
    data['data'] = {
        'money': money,
        'is_all_select': is_select_all
    }
    return JsonResponse(data)
