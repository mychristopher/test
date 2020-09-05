from .models import *

# 算钱的函数
def get_select_money(user):
    # 拿这个人对应的购物车选中商品
    cart_items = Cart.objects.filter(
        user_id=user.id,
        is_select=True
    )
    result = 0
    for i in cart_items:
        # 单价乘以数量
        tmp = i.num * i.goods.price
        result += tmp
    return round(result, 2)