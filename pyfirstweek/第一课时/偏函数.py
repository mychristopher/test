#！/usr/bin/python
# -*- coding: utf-8 -*-

#把一个参数固定住，形成一个新的函数
import functools
int3 = functools.partial(int, base = 2)
print(int3("111"))