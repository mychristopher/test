#！/usr/bin/python
# -*- coding: utf-8 -*-
num = int(input())
if num == 2:
    print("是质数")
index = 2
while index <= num - 1:
    if num % index == 0:
        print("不是质数")
    index += 1

if index == num:
    print("是质数")