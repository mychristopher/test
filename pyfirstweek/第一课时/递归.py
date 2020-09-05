#！/usr/bin/python
# -*- coding: utf-8 -*-
#递归调用：一个函数，调用了自身
#递归函数：一个会调用自身的函数

#方式：写出临界条件;找这一次和上一次的关系;假设当前函数已经能用，调用自身计算上一次的结果，再求出本次的结果

#输入一个数（大于等于1），求1+2+3+...+n的和
"""
def sum1(n):
    sum = 0
    for x in range(1, n + 1):
        sum += x
    return sum
res = sum1(5)
print("res=", res)

"""
def sum2(n):
    if n == 1:
        return 1
    else:
        return n + sum2(n - 1)

res = sum2(5)
print("res =",res)