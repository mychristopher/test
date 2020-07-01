#！/usr/bin/python
# -*- coding: utf-8 -*-
num = 100
while num <= 999:
    a = num % 10
    b = num // 10 % 10
    c = num // 100

    if num == a**3 + b**3 + c**3:
        print(num)
    num += 1