from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r"^home$", home, name="home"),
    url(r"^market/(\d+)/(\d+)/(\d+)", market, name="market"),
    url(r"^cart$", cart, name="cart"),
    url(r"^mine$", mine, name="mine"),
    url(r"^register$", register, name="register"),
    url(r"^login$", login_api, name='login'),
    url(r"^logout$", logout_api, name='logout'),
    url(r"^cart_api$", cart_api),
    url(r"^cartitem_change$", cart_item_change),
    url(r"^cart_item_select$", select_cart_item),
    url(r"^select_all$", select_all)
]