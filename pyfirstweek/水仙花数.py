#！/usr/bin/python
# -*- coding: utf-8 -*-
num=int(input("请输入一个三位数:"))
#153
a=num%10 #取余--个位
b=num//10%10 #取整取余
c=num//100
if num==a**3+b**3+c**3:
    print("这是水仙花数")
else:
    print("非水仙花数")