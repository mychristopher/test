#！/usr/bin/python
# -*- coding: utf-8 -*-
def sum(a,b):
    return a+b

f = sum     #函数是一种数据类型，函数名可以赋值给另一个变量

aa=f(2,3)
print(aa)
res = sum(1,2)     #调用了带有返回值的函数
print(res)
