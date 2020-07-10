#！/usr/bin/python
# -*- coding: utf-8 -*-
#90=2*3*3*5
num = int(input())
i =2
while num!=1:
    if num % i ==0:
        print(i)
        num//=i
    else:
        i += 1