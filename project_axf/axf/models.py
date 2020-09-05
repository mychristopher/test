from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
# axf_wheel(img,name,trackid)


class MyUser(AbstractUser):
    phone = models.CharField(
        max_length=13,
        null=True
    )
    is_delete = models.BooleanField(
        default=False
    )
    icon = models.ImageField(
        upload_to="icons"
    )
    address = models.CharField(
        max_length=200,
        null=True
    )
    email = models.CharField(
        max_length=30,
        unique=True
    )
    class Meta:
        verbose_name="用户"


class BaseData(models.Model):
    img = models.CharField(
        max_length=200
    )
    name = models.CharField(
        max_length=30
    )
    trackid = models.CharField(
        max_length=30
    )
    class Meta:
        # 声明是抽象类
        abstract = True

class MyWheel(BaseData):
    class Meta:
        db_table = "axf_wheel"

class MyNav(BaseData):
    class Meta:
        db_table = "axf_nav"

class MustBuy(BaseData):
    class Meta:
        db_table="axf_mustbuy"
        verbose_name = "必购模型"

class MyShop(BaseData):
    class Meta:
        db_table = "axf_shop"

# axf_mainshow
class MainShow(BaseData):
    categoryid = models.CharField(
        max_length=20
    )
    brandname = models.CharField(
        max_length=50
    )
    img1 = models.CharField(
        max_length=251
    )
    productid1 = models.CharField(
        max_length=10,
        null=True
    )
    childcid1 = models.CharField(
        max_length=20
    )
    longname1 = models.CharField(
        max_length=255
    )
    price1 = models.CharField(
        max_length=15
    )
    marketprice1 = models.CharField(
        max_length=15
    )

    img2 = models.CharField(
        max_length=251
    )
    productid2 = models.CharField(
        max_length=10,
        null=True
    )
    childcid2 = models.CharField(
        max_length=20
    )
    longname2 = models.CharField(
        max_length=255
    )
    price2 = models.CharField(
        max_length=15
    )
    marketprice2 = models.CharField(
        max_length=15
    )

    img3 = models.CharField(
        max_length=251
    )
    productid3 = models.CharField(
        max_length=10,
        null=True
    )
    childcid3 = models.CharField(
        max_length=20
    )
    longname3 = models.CharField(
        max_length=255
    )
    price3 = models.CharField(
        max_length=15
    )
    marketprice3 = models.CharField(
        max_length=15
    )
    class Meta:
        db_table = "axf_mainshow"


class GoodsType(models.Model):
    typeid = models.CharField(
        max_length=10
    )
    typename = models.CharField(
        max_length=20
    )
    childtypenames = models.CharField(
        max_length=251
    )
    typesort = models.IntegerField()

    class Meta:
        db_table = "axf_foodtypes"


class MyGoods(models.Model):
    productid = models.CharField(
        max_length=20
    )
    productimg = models.CharField(
        max_length=255
    )
    productname = models.CharField(
        max_length=100
    )
    productlongname = models.CharField(
        max_length=200
    )
    isxf = models.BooleanField(
        default=0
    )
    pmdesc = models.BooleanField(
        default=0
    )
    specifics = models.CharField(
        max_length=40
    )
    price = models.FloatField()
    marketprice = models.FloatField()
    categoryid = models.IntegerField()
    childcid = models.IntegerField()
    childcidname = models.CharField(
        max_length=100
    )
    dealerid = models.CharField(
        max_length=30
    )
    storenums = models.IntegerField()
    productnum = models.IntegerField()
    class Meta:
        db_table = "axf_goods"


class Cart(models.Model):
    user = models.ForeignKey(
        MyUser
    )
    goods = models.ForeignKey(
        MyGoods
    )
    num = models.IntegerField(
        default=1
    )
    is_select = models.BooleanField(
        default=True
    )