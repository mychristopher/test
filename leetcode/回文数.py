#！/usr/bin/python
# -*- coding: utf-8 -*-
num=int(input("请输入一个五位数:"))
a=num%10
b=num//10000
if a!=b:
    print("不是回文数")
